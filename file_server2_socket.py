
import socket
import os

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "192.168.1.4"
port = 1234

server.bind((host,port))

print("\n Socket is ready at ip {} and port {}".format(host,port))

server.listen()

print("\n Server is ready to listen")

client_socket,client_addr = server.accept()
#print("Socket : ",client_socket)
#print("Client Address : ",client_addr)
path = client_socket.recv(1024).decode()

if os.path.exists(path) and os.path.isfile(path):
    msg = "Okay ready to send your file...."
    client_socket.send(msg.encode())
    client_msg = client_socket.recv(1024).decode()
    print("\n Client : ",client_msg)
    print("\n Sending.......")
    with open(path,"rb") as f:
        r = f.readline()
        while r:
            client_socket.send(r)  #no need to encode bcz it is open in byte format
            r = f.readline()
        print("\n Successfully send....")
        f.close()
            
else:
    msg = "I cannot share this file bcz it is not correct....Sorry"
    client_socket.send(msg.encode())
    
client_socket.close()
