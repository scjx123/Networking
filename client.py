import socket 
import threading,queue
import time 
HOST = "127.0.0.1"
PORT = 9999

def send_data(data):
 s.sendall(bytes(data,"utf-8"))
 data = s.recv (1024) 
 print(data.decode("utf-8")) 

def get_root():
 lock.acquire() 
 with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
  s.connect((HOST,PORT))
  data = "GET /index.html HTTP/1.1 " 
  s.send(bytes(data,"utf-8"))
  rx = s.recv(1024)
  print(rx.decode("utf-8"))
 lock.release()

def get_bio():
 lock.acquire()
 with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
  s.connect((HOST,PORT))
  data = "GET /bio.txt HTTP/1.1" 
  s.send(bytes(data,"utf-8"))
  rx = s.recv(1024)
  print(rx.decode("utf-8"))
 lock.release()

lock = threading.Lock() 
t1 = threading.Thread(target=get_root,args=())
t2 = threading.Thread(target=get_bio,args=())
t1.start()
t2.start()
t1.join()
t2.join()
 
