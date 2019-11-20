import logging
from datetime import datetime


class LogManager:

    def __init__(self):

        # System logs
        self.ERROR_LOG = '.\\logs\\errors.log'
        self.DEBUG_LOG = '.\\logs\\debug.log'
        self.STATUS_LOG = '.\\logs\\info.log'
        self.CRITICAL_LOG = '.\\logs\\critical.log'
        logging.basicConfig(filename=self.STATUS_LOG, level=logging.INFO)
        logging.basicConfig(filename=self.DEBUG_LOG, level=logging.DEBUG)
        logging.basicConfig(filename=self.ERROR_LOG, level=logging.ERROR)
        logging.basicConfig(filename=self.CRITICAL_LOG, level=logging.CRITICAL)
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
