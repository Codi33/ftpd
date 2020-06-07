from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from getpass import getpass

FTP_ADDRESS = input("Enter IP >> ")
FTP_PORT = int(input("Enter Port >> "))
FTP_USER = getpass("Enter Username(not displaying) >> ")
FTP_PASSWORD = getpass("Enter Password(not displaying) >> ")
FTP_DIRECTORY = input("Enter Directory >> ")

print(FTP_ADDRESS, FTP_PORT, FTP_USER, FTP_PASSWORD, FTP_DIRECTORY)

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpd"

    address = (FTP_ADDRESS, FTP_PORT)

    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()