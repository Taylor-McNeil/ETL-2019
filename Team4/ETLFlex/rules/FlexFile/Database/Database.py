import mysql.connector
import pandas as pd


class Database:

    def __init__(self):
        # Database metadata
        self._db_name = 'flex_db'
        self._host = 'localhost'
        self._user = 'root'
        self._passwd = 'Poland1997'

        # Table names
        self._file_master = 'file_master'
        self._col_master = 'col_master'
        self._data_master = 'data_master'
        self._date_master = 'date_master'

        # Database connection
        self.conn = self.connect_db()
        self.cur = self.conn.cursor()

    def get_conns(self):
        all_conns = []
        query = 'SELECT file_name,src,src_type,dir,username,pass_key FROM ' + self._file_master
        df = pd.read_sql(query, self.conn)
        for i in df.index:
            all_conns.append(df.iloc[i].to_dict())
        return all_conns

    def get_rules(self):
        rules = []
        query = 'SELECT file_id,file_name,last_update FROM ' + self._file_master
        df = pd.read_sql(query, self.conn)
        for i in df.index:
            rules.append(df.iloc[i].to_dict())
        return rules

    def get_file_history(self, data):
        _file_name = data['file_name']       # OR file_id
        file_history = []
        query = 'SELECT date_uploaded,num_of_rows FROM ' + self._date_master + ' WHERE file_name = ' + _file_name
        df = pd.read_sql(query, self.conn)
        for i in df.index:
            file_history.append(df.iloc[i].to_dict())
        return file_history

    def get_file_data(self, data):
        file_data = []
        query = 'SELECT file_id FROM ' + self._file_master + ' WHERE file_name = %s'
        prevent_inject = (data['file_name'],)
        self.cur.execute(query, prevent_inject)
        result = self.cur.fetchall()
        _file_id = result[0][0]

        # Gather data and format for view -- use new data frame
        query = 'SELECT col_num,col_name FROM ' + self._col_master + ' WHERE file_id = ' + str(_file_id)
        df_col = pd.read_sql(query, self.conn)
        col_headers = list(df_col['col_name'])

        query = 'SELECT col_num,row_num,value FROM ' + self._data_master + ' WHERE file_id = ' + str(_file_id)
        df_values = pd.read_sql(query, self.conn)

        temp = []
        for i in range(1, len(df_col.index) + 1):
            df_temp = df_values.loc[df_values['col_num'] == str(i)]
            temp.append(list(df_temp['value']))

        temp_dict = {}
        for i in range(len(df_col.index)):
            temp_dict[col_headers[i]] = temp[i]

        df_final = pd.DataFrame(temp_dict)
        # print(df_final)

        for i in df_final.index:
            file_data.append(df_final.iloc[i].to_dict())

        return file_data

    def connect_db(self):
        connection = mysql.connector.connect(
            host=self._host,
            user=self._user,
            passwd=self._passwd,
            database=self._db_name
        )
        return connection

    def create_db(self, db_name):
        try:
            new_db_connect = mysql.connector.connect(
                host=self._host,
                user=self._user,
                passwd=self._passwd
            )
            cursor = new_db_connect.cursor()
            cursor.execute('CREATE DATABASE ' + db_name)
            cursor.close()
            new_db_connect.close()
        except mysql.connector.errors:
            print('A database already exists with that name.')

    @staticmethod
    def create_table(connection, table_name, col_data):
        stmt = 'CREATE TABLE ' + table_name + ' ('
        query = ''

        for key, value in col_data.items():
            query += key + ' ' + value + ', '

        query = stmt + query[:-2] + ')'
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()

    @staticmethod
    def update_table(connection, table_name, row_data):
        r = row_data[0]
        stmt = 'INSERT INTO ' + table_name + ' (' + r[0] + ', ' + r[1] + ', ' + r[2] + ') VALUES( %s, %s, %s)'
        cursor = connection.cursor()
        for i in range(1, len(row_data)):
            l = []
            temp = row_data[i]
            # print(temp)
            for item in temp:
                l.append(item)
                # print(item)
            val = (l[0], l[1], l[2])
            cursor.execute(stmt, val)
            connection.commit()
        cursor.close()

    @staticmethod
    def view_table_data(self, table_name):
        query = 'SELECT * FROM ' + table_name
        df = pd.read_sql(query, self.conn)
        view = pd.DataFrame(df)
        return view


def main():
    db = Database()
    db.get_conns()


# main()
