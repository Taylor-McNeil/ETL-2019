import mysql.connector
import pandas as pd
from datetime import datetime
import time


class Database:

    def __init__(self):
        # Database metadata
        self._db_name = 'flex_db'
        self._host = 'localhost'
        self._user = 'root'
        self._passwd = '1qaz@WSX3edc$RFV'

        # Table names
        self._file_master = 'file_master'
        self._col_master = 'col_master'
        self._data_master = 'data_master'
        self._date_master = 'date_master'

        # Database connection
        self.conn = self.connect_db()
        self.cur = self.conn.cursor()

    # Testing Only - Display data_master table in a data frame
    def test(self):
        query = 'SELECT * FROM ' + self._data_master + ' WHERE file_id = 3'
        df = pd.read_sql(query, self.conn)
        df1 = df.isna().any(axis=1)
        print(df)
        print()

    # For single file sync
    def get_conn(self, file_name):
        query = 'SELECT src,src_type,dir,username,pass_key FROM ' + self._file_master + ' WHERE file_name = %s'
        df = pd.read_sql(query, self.conn, params=(file_name,))
        return df.iloc[0].to_dict()

    # For full sync - Grab all repository info from DB for creating connections
    def get_conns(self):
        all_conns = []
        query = 'SELECT file_name,src,src_type,dir,username,pass_key FROM ' + self._file_master
        df = pd.read_sql(query, self.conn)
        for i in df.index:
            all_conns.append(df.iloc[i].to_dict())
        return all_conns

    # Get single rule for dashboard (after sync update)
    def get_rule_after_sync(self, file_name):
        temp = []
        query = 'SELECT file_id,file_name,last_update FROM ' + self._file_master + ' WHERE file_name = %s'
        df = pd.read_sql(query, self.conn, params=(file_name,))
        for i in df.index:
            temp.append(df.iloc[i].to_dict())

        output = self.output_refactor(temp)
        return output[0]

    # Get all rules for dashboard
    def get_rules(self):
        temp = []
        query = 'SELECT file_id,file_name,last_update FROM ' + self._file_master
        df = pd.read_sql(query, self.conn)
        for i in df.index:
            temp.append(df.iloc[i].to_dict())

        output = self.output_refactor(temp)
        return output

    # Get file history - displays file upload dates and number of rows added to DB
    def get_file_history(self, data):
        _file_name = data['file_name']      # OR file_id
        file_history = []
        query = 'SELECT date_uploaded,num_of_rows FROM ' + self._date_master + ' WHERE file_name = %s'
        df = pd.read_sql(query, self.conn, params=(_file_name,))
        for i in df.index:
            file_history.append(df.iloc[i].to_dict())

        output = self.output_refactor(file_history)
        return output

    def get_file_data(self, data):
        file_data = []
        _file_name = data['file_name']
        # date_uploaded = datetime.strptime(data['date_uploaded'], '%Y-%m-%d %H:%M:%S')
        date_uploaded = data['date_uploaded']
        query = 'SELECT file_id FROM ' + self._file_master + ' WHERE file_name = %s'
        prevent_inject = (_file_name,)
        self.cur.execute(query, prevent_inject)
        result = self.cur.fetchall()
        _file_id = result[0][0]

        # Gather data and format for view -- use new data frame
        query = 'SELECT col_num,col_name FROM ' + self._col_master + ' WHERE file_id = %s'
        df_col = pd.read_sql(query, self.conn, params=(str(_file_id)))
        col_headers = list(df_col['col_name'])

        query = 'SELECT col_num,row_num,value FROM ' \
                + self._data_master + ' WHERE file_id = %s AND date_uploaded = %s'
        df_values = pd.read_sql(query, self.conn, params=(str(_file_id), date_uploaded))

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

        output = self.output_refactor(file_data)
        return output

    def connect_db(self):
        connection = mysql.connector.connect(
            host=self._host,
            user=self._user,
            passwd=self._passwd,
            database=self._db_name
        )
        return connection

    @staticmethod
    def output_refactor(data):
        rules = []
        for record in data:
            rule_dict = {}
            for key, val in record.items():
                rule_dict[str(key)] = str(val)
            rules.append(rule_dict)
        return rules

    # Methods below here are for testing
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
    db.test()


# main()
