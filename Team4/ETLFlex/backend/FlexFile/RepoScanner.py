from FTP_Connect import FTP_Connect
from Database.Database import Database
from Admin import Admin
import pandas as pd
import ftplib
import pathlib
import urllib.request
import shutil
from datetime import datetime


class RepoScanner:

    def __init__(self):
        # File data
        self.file_list = []
        self.column_list = []
        self.proc_file_list = []
        self.proc_directory = './processed_files/'
        self.result = False
        self.response = False

        # Create db connection
        self.db = Database()
        self.conns = []

        # User attributes
        self.user = ''
        self._pass_key = ''

        # FTP attributes
        self.ftp_file_list = []
        self.ftp_instance = None
        self.ftps = None
        self.pwd = ''

        # Web link attributes
        self.url = ''

        # Date
        self.now = datetime.now().strftime('%Y%m%d')

    def run_scanner(self):
        self.conns = self.db.get_conns()
        for conn in self.conns:
            self.file_list.append(conn['file_name'])

            # Scanner on FTP
            if str(conn['src_type']).lower() == 'ftp':
                self.ftp_instance = FTP_Connect(conn['src'], conn['username'], conn['pass_key'], conn['dir'])
                self.ftps = self.ftp_instance.ftp_conn()
                self.pwd = self.ftps.pwd()
                self.read_ftp_file_names()
                self.download_ftp_files()
                self.call_admin()

            # Scanner on web link
            if str(conn['src_type']).lower() == 'url':
                # self.url = conn['src']
                # try:
                #     with urllib.request.urlopen(conn['src']) as response, open('.\\downloads\\' +
                #                                                                str(conn['file_name']),
                #                                                                'wb') as out_file:
                #         shutil.copyfileobj(response, out_file)
                # except urllib.request.HTTPError as e:
                #     print(e)
                self.call_admin()

            # Scanner on local file system
            if str(conn['src_type']).lower() == 'local':
                # do something
                pass

        return self.response

    def read_ftp_file_names(self):
        # Acquiring file names in specified directory
        try:
            self.ftp_file_list = self.ftps.nlst()  # list of files in directory
            # self.ftps.cwd(self.proc_directory)
            # self.proc_file_list = self.ftps.nlst()
            # self.ftps.cwd('..')
        except ftplib.error_perm as resp:
            print(resp)

        self.ftp_file_list = [x for x in self.ftp_file_list if str(x).endswith('.txt') or
                              str(x).endswith('.csv') or str(x).endswith('.xlsx') or str(x).endswith('.xls')]

    def download_ftp_files(self):
        # Download files from ftp
        for file in self.file_list:
            if file in self.ftp_file_list:
                try:
                    # Write file
                    self.ftps.retrbinary('RETR ' + self.pwd + '/' + file, open('.\\downloads\\' + file, 'wb').write)
                except ftplib.all_errors as e:
                    print(e)

    def move_ftp_files(self, file):
        # Method to move files that have been downloaded
        try:
            if self.result:
                self.ftps.rename(self.pwd + '/' + file, self.pwd + '/processed_files/' + str(self.now) + '_' + file)
        except ftplib.all_errors as e:
            print(e)

    def call_admin(self):
        csv_ext = ['.txt', '.csv']
        xlsx_ext = ['.xlsx', '.xls']

        for file in self.file_list:
            index = str(file).index('.')
            file_ext = str(file)[index:]

            try:
                read_file = None
                if file_ext in csv_ext:
                    read_file = pd.read_csv('.\\downloads\\' + file, encoding='ISO-8859-1')
                elif file_ext in xlsx_ext:
                    read_file = pd.read_excel('.\\downloads\\' + file)

                # Grab column headers from file
                self.column_list = list(read_file.columns)

                data = {
                    'file_name': file,
                    'col': self.column_list
                }

                admin = Admin(data)
                self.result = admin.check_for_file()

                # If we want to delete file from system
                if self.result:
                    self.response = True
                    try:
                        rmv = pathlib.Path('.\\downloads\\' + file)
                        rmv.unlink()
                        if file in self.ftp_file_list:
                            self.move_ftp_files(file)
                    except WindowsError as e:
                        # Place error log
                        print(e)
                else:
                    continue
                self.result = False
            except FileNotFoundError:
                continue
        self.file_list.clear()

#     self.ftps.close()


def main():
    rs = RepoScanner()
    rs.run_scanner()

# main()
