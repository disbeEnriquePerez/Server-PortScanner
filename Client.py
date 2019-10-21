#!/usr/bin/python3
# RUN THIS PROGRAM ON ANOTHER COMUTER  AND MAKE SURE SERVER.PY 
# IS RUNNNING AND IT WILL CONNECT WITH EACH OTHER
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#this is the ip address of the computer you want to connect to 
#DONT CHANGE 
host = '192.168.1.16'

port = 444

clientsocket.connect(host, port)

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
