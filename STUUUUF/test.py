from Database.UserDatabase import UserDatabase
from FTP_Connect import FTP_Connect


def main():

    # Create new user
    print('Name: ')
    user = input()

    print('Server address: ')
    ftp_server = input()

    print('FTP username: ')
    ftp_username = input()

    print('FTP password: ')
    ftp_passwd = input()

    print('Directory to scan: ')
    ftp_directory = input()

    # -------------------------------------------------------------------- #

    # Create rule
    print('\nEnter first rule...')
    print()

    print('Name of file: ')
    name_of_file = input()

    print('What would you like to name the table: ')
    table_name = input()

    print('Number of columns: ')
    num_of_columns = int(input())

    field_names = {}
    for _ in range(0, num_of_columns):
        print('Enter column header name: ')
        name = input()

        print('Enter data type: ')
        print('E.g. INT(255), VARCHAR(255), FLOAT(size,d)')
        data_type = input()
        field_names[name] = data_type

    # --------------------------------------------------------------------- #

    # Connect to FTP
    f = FTP_Connect(ftp_server, ftp_username, ftp_passwd, ftp_directory)
    conn = f.ftp_conn()

    # Scan FTP for files return file names
    files = f.read_file_names(conn)

    f.download_files(conn, files)

    # Parse file
    row_data = f.parse_file(name_of_file)

    conn.close()

    # ------------------------------------------------------------------------ #

    # DB instance
    db = UserDatabase()

    # create DB
    db.create_db(user)

    # connect to DB with user db name as parameter
    connect = db.connect_db(user)
    print('\nConnected to Database...')

    # # table name
    # table_name = 'test_table'

    # table data
    # col_data = {'id': 'INT AUTO_INCREMENT PRIMARY KEY', 'name': 'VARCHAR(255)'}

    # create table
    db.create_table(connect, table_name, field_names)

    # create cursor and show databases on server
    cursor = connect.cursor()
    cursor.execute('SHOW DATABASES')

    for x in cursor:
        print(x)

    # view table
    view = db.view_table_data(connect, table_name)
    print(view)

    # db.update_table(connect, table_name, row_data)

    db.view_table_data(connect, table_name)

    cursor.close()
    connect.close()


main()
