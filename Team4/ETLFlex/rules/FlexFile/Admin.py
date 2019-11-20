from Database.Database import Database
import pandas as pd
from logmanager import LogManager
from datetime import datetime


# Contains rule checking and writes to DB
class Admin:

    # Unpack data structure to collect user input
    def __init__(self, data_capture):
        self.data = {}
        for key, val in data_capture.items():
            if val == '':
                self.data[key] = None
            else:
                self.data[key] = val

        self.file_name = self.data['file_name']
        if self.data['col']:
            self.columns_from_file = self.data['col']
            self.received_col_num = len(self.columns_from_file)

        try:
            if self.data['file_id']:
                self.file_id = self.data['file_id']
        except KeyError:
            self.file_id = 0

        # Log Manager
        self.logm = LogManager()

        # Database and table names
        self._db_name = 'flex_db'
        self._file_master = 'file_master'
        self._col_master = 'col_master'
        self._data_master = 'data_master'

        # Create connection
        self.db = Database()

        # Table attributes
        self.col_num = ''
        self.col_name = ''
        self.num_cols = 0
        self.last_upload = ''
        self.source = ''
        self.directory = ''
        self.src_type = ''
        self.username = ''
        self._pass_key = ''

        # File attributes
        self.file_ext = ''
        self.downloads_dir = '.\\downloads\\'
        self.now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def check_filename(self):
        # Pull record matching file_name from file_master
        _query = 'SELECT * FROM ' + self._file_master + ' WHERE file_name = %s'
        _prevent_inject = (self.file_name,)
        self.db.cur.execute(_query, _prevent_inject)
        result = self.db.cur.fetchall()

        # If record exists, extract data
        if result:
            self.file_id = result[0][0]
            self.file_name = result[0][1]
            self.num_cols = int(result[0][2])
            return True
        else:
            return False

    def check_num_cols(self):
        if self.received_col_num == self.num_cols:
            return True
        else:
            return False

    def check_col_names(self):
        # Pull column names from column_master where file_id is matched
        _query = 'SELECT col_name FROM ' + self._col_master + ' WHERE file_id = %s'
        _prevent_inject = (self.file_id,)
        self.db.cur.execute(_query, _prevent_inject)
        result = self.db.cur.fetchall()

        column_list = []
        for column in result:
            column_list.append(list(column)[0])

        if sorted(column_list) == sorted(self.columns_from_file):
            return True
        else:
            return False

    def write_rule(self):
        # If rule does not exist, method to write rule
        self.source = self.data['src']
        self.directory = self.data['directory']
        self.src_type = self.data['type']
        self.username = self.data['username']
        self._pass_key = self.data['password']

        with open('.\\config\\last_fileid.txt', 'r') as f:
            self.file_id = int(f.read()) + 1

        _query = 'INSERT INTO file_master (file_id, file_name, num_cols, last_update, src, src_type, dir, username,' \
                 'pass_key) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        _prevent_inject = (self.file_id, self.file_name, str(self.received_col_num), None, self.source, self.src_type,
                           self.directory, self.username, self._pass_key)

        try:
            self.db.cur.execute(_query, _prevent_inject)
        except RuntimeError as e:
            return e

        self.col_num = 1
        for i in range(self.received_col_num):
            self.col_name = self.columns_from_file[i]
            _query = 'INSERT INTO col_master (file_id, col_num, col_name) VALUES (%s, %s, %s)'
            _prevent_inject = (self.file_id, str(self.col_num), self.col_name)
            self.col_num += 1
            self.db.cur.execute(_query, _prevent_inject)

        self.db.conn.commit()
        # self.db.cur.close()

        with open('.\\config\\last_fileid.txt', 'w') as f:
            f.write(str(self.file_id))

        self.col_num = 1
        self.col_name = ''

    def write_file(self):
        _query = 'SELECT file_id FROM file_master WHERE file_name = (%s)'
        _prevent_inject = (self.file_name,)
        self.db.cur.execute(_query, _prevent_inject)
        temp = self.db.cur.fetchone()
        self.file_id = int(temp[0])

        csv_ext = ['.txt', '.csv']
        xlsx_ext = ['.xlsx', 'xls']
        index = str(self.file_name).index('.')
        self.file_ext = str(self.file_name)[index:]

        read_file = None
        if self.file_ext in csv_ext:
            read_file = pd.read_csv(self.downloads_dir + str(self.file_name))
        elif self.file_ext in xlsx_ext:
            read_file = pd.read_excel(self.downloads_dir + str(self.file_name))
        df = pd.DataFrame(read_file)
        number_of_rows = len(df.index)

        self.col_num = 0
        for row in range(number_of_rows):
            for col in range(self.received_col_num):
                query = 'INSERT INTO data_master (file_id, col_num, row_num, value) VALUES ' \
                        '(%s, %s, %s, %s)'
                prevent_inject = (self.file_id, str(self.col_num + 1), str(row + 1),
                                  str(df.iloc[row][self.columns_from_file[col]]))
                self.col_num += 1
                self.db.cur.execute(query, prevent_inject)
            self.col_num = 0

        self.db.conn.commit()
        self.col_num = 1
        self.col_name = ''

        _query = 'UPDATE file_master SET last_update = (%s) WHERE file_id = (%s)'
        _prevent_inject = (str(self.now), str(self.file_id))
        self.db.cur.execute(_query, _prevent_inject)
        self.db.conn.commit()

        _query = 'INSERT INTO date_master (file_name, date_uploaded, num_of_rows) VALUES ' \
                 '(%s, %s, %s)'
        _prevent_inject = (self.file_name, str(self.now), str(number_of_rows))
        self.db.cur.execute(_query, _prevent_inject)
        self.db.conn.commit()
        self.db.cur.close()

    def run_rule_check(self):
        return self.check_filename() and self.check_num_cols() and self.check_col_names()

    def check_for_file(self):
        result = self.run_rule_check()
        if result:
            # Write file
            self.write_file()
            self.logm.successful_file_upload(self.file_name)
            return result
        else:
            self.logm.rule_dne(self.file_name)
            return result

    def check_for_rule(self):
        result = self.run_rule_check()
        if not result:
            # Write rule - rule does not exist
            self.write_rule()
            self.logm.successful_rule_submission(self.file_name)
            return result
        else:
            # Rule already exists
            self.logm.rule_exists(self.file_name)
            return result
