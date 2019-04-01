#!/usr/bin/python

import socket
import sys

# Take an argument from the user
if len(sys.argv) != 2:
    print "Usage: vrfy.py <username>"
    sys.exit(0)

# Create a Socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the Server 
connect=s.connect(('192.168.43.23' ,25))
# Receive the banner
banner =s.recv(1024)
# VRFY a user
s.send('VRFY ' + sys.argv[1] + '\r\n') 
result=s.recv(1024)
print result 
# Close the socket
s.close()