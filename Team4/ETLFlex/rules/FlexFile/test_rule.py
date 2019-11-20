from Admin import Admin
from RepoScanner import RepoScanner
from Database.Database import Database


def main():
    # data = {
    #     'src': 'https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv',
    #     'directory': '',
    #     'type': 'web link',
    #     'username': '',
    #     'password': '',
    #     'file_name': 'sample_web_file.csv',
    #     'col': ['product', 'name', 'num_items', 'balance', 'price', 'cogs', 'mfg', 'type', 'percent']
    # }

    data = {'file_name': 'f1.txt'}
    db = Database()
    print(db.get_file_data(data))
    # admin = Admin(data)
    # # submit rule
    # admin.check_for_rule()

    # sync
    # rs = RepoScanner()
    # rs.run_scanner()


main()

