import socket 
import time 
HOST = "127.0.0.1"
PORT = 9999

def send_data(data):
 s.sendall(bytes(data,"utf-8"))
 data = s.recv (1024) 
 print(data.decode("utf-8")) 


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: 
 s.connect((HOST,PORT))
 data = "GET /index.html HTTP/1.1" 
 s.send(bytes(data,"utf-8"))
 data = s.recv (1024) 
 print(data.decode("utf-8")) 
 
#s.connect((HOST,PORT))
 data = "GET /bio.txt HTTP/1.1" 
 s.send(bytes(data,"utf-8"))
 data = s.recv (1024) 
 print(data.decode("utf-8")) 

