from Team4.ETLFlex.rules.FlexFile.Database.Database import Database
from Team4.ETLFlex.rules.FlexFile.Admin import Admin
from Team4.ETLFlex.rules.FlexFile.RepoScanner import RepoScanner
import json
import timeit


def main():
    # Submit rule data structure
    data = {
        'src': 'localhost',
        'directory': '/files/',
        'type': 'ftp',
        'username': 'flexuser',
        'password': 'hello1',
        'file_name': 'mass_dataset.csv',
        'col': ['Region', 'Country', 'Item_Type', 'Sales_Channel', 'Order_Priority', 'Order_Date', 'Order_ID',
                'Ship_Date', 'Units_Sold', 'Unit_Price', 'Unit_Cost', 'Total_Revenue', 'Total_Cost', 'Total_Profit']

    }

    # Rule, history, file_data retrieval data structure
    # data = {'file_name': 'f1.txt',
    #         'date_uploaded': '2019-11-19 19:23:02'
    #         }

    # Database retrieval test
    # db = Database()
    # print(db.get_file_history(data))
    # print(db.get_file_history(data))
    # print(db.get_rules())

    # Admin test for rule submission
    # admin = Admin(data)
    # admin.check_for_rule()

    # Sync test
    def code_to_test():
        rs = RepoScanner()
        rs.run_scanner()

    elapsed_time = timeit.timeit(code_to_test, number=100)/100
    print('{} seconds'.format(elapsed_time))


# main()

