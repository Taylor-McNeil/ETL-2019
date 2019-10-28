from Database.UserDatabase import UserDatabase


# Contains rule checking and writes to DB
class Admin:

    # Database and table names
    db_name = 'flex_db'
    file_master = 'file_master'
    col_master = 'col_master'
    data_master = 'data_master'

    # Column master attributes
    file_id = 0
    col_num = ''
    col_name = ''

    # File master attributes
    file_name = ''
    num_cols = 0

    # Data master attributes
    row_num = 0
    value = ''

    # SQL fields
    query = ''
    prevent_inject = ()

    # Create connection
    db = UserDatabase()
    conn = db.connect_db(db_name)
    cur = conn.cursor()

    def __init__(self, file, columns_from_file):
        self.file = file
        self.columns_from_file = columns_from_file

    def check_filename(self):
        query = 'SELECT * FROM ' + self.file_master + ' WHERE file_name = %s'
        prevent_inject = (self.file,)
        self.cur.execute(query, prevent_inject)
        result = self.cur.fetchall()
        if result:
            self.file_id = result[0][0]
            self.file_name = result[0][1]
            self.num_cols = int(result[0][2])
            return True
        else:
            return False

    def check_num_cols(self):
        if len(self.columns_from_file) == self.num_cols:
            return True
        else:
            return False

    def check_col_names(self):
        query = 'SELECT col_name FROM ' + self.col_master + ' WHERE file_id = %s'
        prevent_inject = (self.file_id,)
        self.cur.execute(query, prevent_inject)
        result = self.cur.fetchall()

        column_list = []
        for column in result:
            column_list.append(list(column)[0])

        if column_list.sort() == self.columns_from_file.sort():
            return True
        else:
            return False


file_list = ['f1.txt', 'f2.txt']    # Passed from Scanner
col_list = [['name', 'age', 'profession'], ['stock', 'price']]
rc = Admin(file_list[0], col_list[0])

if rc.check_filename() and rc.check_num_cols() and rc.check_col_names():
    print('Rule matched.')
else:
    print('Rule not matched.')




