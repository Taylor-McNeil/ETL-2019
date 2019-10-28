import mysql.connector
import pandas as pd
import numpy as np


class UserDatabase:
    is_connected = False
    _host = 'localhost'
    _user = 'root'
    _passwd = '1qaz@WSX3edc$RFV'

    def __init__(self):
        # self.user = user
        pass

    def connect_db(self, db_name):
        connection = mysql.connector.connect(
            host=self._host,
            user=self._user,
            passwd=self._passwd,
            database=db_name
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
    def view_table_data(connection, table_name):
        query = 'SELECT * FROM ' + table_name
        df = pd.read_sql(query, connection)
        view = pd.DataFrame(df)
        # view = np.vstack([df.columns, df.values])
        return view.transpose()


def main():
    db = UserDatabase()

    # create DB
    # db.create_db('test_db')

    # connect to DB with user db name as parameter
    connect = db.connect_db('flex_db')

    # create cursor and show databases on server
    cursor = connect.cursor()
    # cursor.execute('SHOW DATABASES')
    #
    # for x in cursor:
    #     print(x)

    # view table
    view = db.view_table_data(connect, 'data_master')
    print(view)

    cursor.close()
    connect.close()


main()
