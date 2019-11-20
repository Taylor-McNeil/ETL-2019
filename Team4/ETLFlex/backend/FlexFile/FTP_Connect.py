import ftp_utility


class FTP_Connect:

    def __init__(self, host, username, passwd, dir):
        self._host = host
        self._username = username
        self._passwd = passwd
        self._directory = dir

    # Opening FTP connection
    def ftp_conn(self):
        ftps = ftp_utility.MyFTP_TLS(self._host)
        ftps.auth()
        ftps.prot_p()
        ftps.login(self._username, self._passwd)
        ftps.cwd(self._directory)
        return ftps

