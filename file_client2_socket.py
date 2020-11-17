
import socket
import os

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "192.168.1.4"
port = 1234

server.connect((host,port))

path = input("\n Enter your path separated by (/,//,\\) : ")

server.send(path.encode())

s_msg = server.recv(1024).decode()
print("Server Message : ",s_msg)

if "/" in path:
    filename = path.split("/")[-1]
elif "//" in path:
    filename = path.split("//")[-1]
elif "\\" in path:
    filename = path.split("\\")[-1]

newpath = input("\n Enter the path where you want to save the file : ")

newpath = os.path.join(newpath,filename)

server.send("I am ready to receive".encode())

with open(newpath,"wb") as f:
    l = server.recv(1024)
    while l:
        f.write(l)
        l = server.recv(1024)
    f.close()
    print("\n Received file ......")

server.close()
