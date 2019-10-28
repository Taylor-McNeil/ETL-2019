import ftplib
import ftp_utility
import csv
import pandas as pd
import os


class FTP_Connect:

    # _host = 'localhost'
    # _username = 'flexuser'
    # _passwd = 'hello1'
    # _directory = '/files/'

    def __init__(self, _host, _username, _passwd, _directory):
        self._host = _host
        self._username = _username
        self._passwd = _passwd
        self._directory = _directory

    # Opening FTP connection
    def ftp_conn(self):

        ftps = ftp_utility.MyFTP_TLS(self._host)
        ftps.auth()
        ftps.prot_p()
        ftps.login(self._username, self._passwd)
        ftps.cwd(self._directory)

        # Check present working directory
        print('pwd:', ftps.pwd())
        # read_files(ftps)
        return ftps

    # Temporary file reader
    @staticmethod
    def read_file_names(ftps):
        # Acquiring file names in specified directory
        file_list = []
        try:
            print('Retrieving Files...')
            file_list = ftps.nlst()             # list of files in directory
            print(file_list)
            print()
        except ftplib.error_perm as resp:
            print(resp)

        return file_list

    @staticmethod
    def download_files(ftps, files):
        pwd = ftps.pwd()

        for file in files:
            try:
                # Scan file without downloading
                # ftps.retrlines('RETR ' + pwd + '/' + file, row_data.append(csv.reader))

                # Write to file
                ftps.retrbinary('RETR ' + pwd + '/' + file, open(file, 'wb').write)

                # If we want to delete file from system
                # path = os.path.dirname(os.path.realpath(file))
                # os.remove(path)
            except ftplib.all_errors as e:
                print(e)

    @staticmethod
    def parse_file(file):

        # This will eventually run per 1 file
        # for file in files:
        row_data = []
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                row_data.append(row)

        field_names = row_data[0]
        df = pd.read_csv(file)
        print(df)
        print()

        col_data = []
        for field in field_names:
            name = field
            col_data.append(df[name])

        # for item in col_data[0]:
        #     print(item)

        return row_data


# f = FTP_Connect('localhost', 'flexuser', 'hello1', '/files/')
# conn = f.ftp_conn()
# files = f.read_file_names(conn)
# f.download_files(conn, files)
# f.parse_file(files)
# conn.close()


