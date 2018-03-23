import getpass
import paramiko

# Open a transport
host = raw_input("Enter hostname: ")
port = raw_input("Enter port number: ")
transport = paramiko.transport.Transport(host, port)

# Auth
username = raw_input("Username: ")
password = getpass.getpass("Enter password:")
transport.connect(username = username, password = password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)

## Download
#filepath = '/etc/passwd'
#localpath = '/home/remotepasswd'
#sftp.get(filepath, localpath)

## Upload
local_filepath = ''
remote_filepath = ''
sftp.put(localpath, filepath)

## Close
sftp.close()
transport.close()