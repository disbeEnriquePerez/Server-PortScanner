#!/usr/bin/python3
import socket 

# creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get SERVER'S IP address one of two ways 
host = socket.gethostname()
#or
#host = '192.168.1.16'
##############################

port = 444 

# binding to the socket
serversocket.bind((host, port))

#Starting TCP listener
serversocket.listen(3)

while True:
    # Starting the connection
    clientsocket, address = serversocket.accept()
    print("received connection from %s " % str(address))
    message = 'Hello! thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()