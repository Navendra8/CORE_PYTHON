
import socket
import os

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "192.168.1.4"
port = 1234

server.connect((host,port))

path = input("\n Enter your path : ")

server.send(path.encode())

s_msg = server.recv(1024).decode()
print("Server Message : ",s_msg)
