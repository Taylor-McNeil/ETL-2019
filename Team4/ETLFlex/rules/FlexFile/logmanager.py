import logging
from datetime import datetime


class LogManager:

    def __init__(self):
        self.logs_path = '.\\rules\\FlexFile\\logs\\'

        # FOR FRANKIE'S SYSTEM
        # self.logs_path = 'c:\\swe\\ETL-2019\\Team4\\ETLFlex\\rules\\FlexFile\\logs\\'

        # System logs
        self.ERROR_LOG = self.logs_path + 'errors.log'
        self.DEBUG_LOG = self.logs_path + 'debug.log'
        self.STATUS_LOG = self.logs_path + 'info.log'
        self.CRITICAL_LOG = self.logs_path + 'critical.log'
        logging.basicConfig(filename=self.STATUS_LOG, level=logging.INFO)
        logging.basicConfig(filename=self.DEBUG_LOG, level=logging.DEBUG)
        logging.basicConfig(filename=self.ERROR_LOG, level=logging.ERROR)
        logging.basicConfig(filename=self.CRITICAL_LOG, level=logging.CRITICAL)

        # Date
        self.now = datetime.now()

    def successful_file_upload(self, file_name):
        logging.info(str(self.now.strftime('%m/%d/%Y, %H:%M:%S')) + ' : ' + file_name +
                     ' successfully uploaded to database')

    def rule_exists(self, file_name):
        logging.info(str(self.now.strftime('%m/%d/%Y, %H:%M:%S')) + ' : ' +
                     'rule already exists in database for ' + file_name)

    def successful_rule_submission(self, file_name):
        logging.info(str(self.now.strftime('%m/%d/%Y, %H:%M:%S')) + ' : ' +
                     'rule submission successful for ' + file_name)

    def rule_dne(self, file_name):
        logging.info(str(self.now.strftime('%m/%d/%Y, %H:%M:%S')) + ' : ' +
                     'rule match does not exist, create new rule for ' + file_name)
