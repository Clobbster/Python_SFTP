####################################################
#Python SSH Client --CR --2018
####################################################

'''
This is my first iteration of using paramiko. I'm using this
as a test framework for the SFTP client to come.
'''

import getpass
import paramiko
import sys

username = raw_input("Username: ")    
password = getpass.getpass("Password: ")    
hostname = raw_input("Target_IP: ")   
port = raw_input("Target_Port: ")     

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname=hostname,
               port=port, 
               username=username,
               password=password
               )

stdin, stdout, stderr = client.exec_command('ls  ./Desktop|head -n 5')
print "STDOUT:\n%s\n\nSTDERR:\n%s\n" %( stdout.read(), stderr.read() )
