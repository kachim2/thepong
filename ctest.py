# Import socket module
import socket
  
# Create a socket object
s = socket.socket()
  
# Define the port on which you want to connect
port = 40674
  
# connect to the server on local computer
s.connect(('127.0.0.1', port))
  
# receive data from the server
print(int.from_bytes( s.recv(64), "little"))
  
# close the connection
s.close()