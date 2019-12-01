from .Database.Database import Database
from .Admin import Admin
from .RepoScanner import RepoScanner
import json
import timeit


def main():
    # Submit rule data structure
    # data = {
    #     'src': 'localhost',
    #     'directory': '/files/',
    #     'type': 'ftp',
    #     'username': 'flexuser',
    #     'password': 'hello1',
    #     'file_name': 'mass_dataset.csv',
    #     'col': ['Region', 'Country', 'Item_Type', 'Sales_Channel', 'Order_Priority', 'Order_Date', 'Order_ID',
    #             'Ship_Date', 'Units_Sold', 'Unit_Price', 'Unit_Cost', 'Total_Revenue', 'Total_Cost', 'Total_Profit']
    #
    # }

    # Rule, history, file_data retrieval data structure
    data = {
        "file_name": "f1.txt",
        "date_uploaded": "2019-11-28 22:42:57"
    }

    rs = RepoScanner()
    rs.file_sync(data['file_name'])

    # Database retrieval test
    # db = Database()
    # print(db.get_file_history(data))
    # db.get_conn(data['file_name'])
    # print(db.get_rules())

    # Admin test for rule submission
    # admin = Admin(data)
    # admin.check_for_rule()

    # Sync test
    # def code_to_test():
    #     rs = RepoScanner()
    #     rs.file_sync(data['file_name'])
    #
    # elapsed_time = timeit.timeit(code_to_test, number=100)/100
    # print('{} seconds'.format(elapsed_time))


#main()
