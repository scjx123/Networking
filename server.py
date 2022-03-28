import socket 
import codecs
import threading,queue 

HOST = "0.0.0.0"
PORT = 9999
q = queue.Queue()
conn = None
def header_gen(type,len):
 return "HTTP/1.1 200 OK\r\n Connection: close\r\n Content-Type: {}\r\n Content-Length: {}\r\n\r\n".format(type,len) 


def Producer(s):
 global conn 
 while True: 
  conn,addr=s.accept()
  req = conn.recv(1024).decode()
  print(req)
  q.put(req) 
 
def Consumer(): 
 #Consumer 
 global conn
 while True:
  req = q.get(block=True)
  type = "" 
  if "bio.txt" in req:
   fin=codecs.open("bio.txt","r",encoding="utf-8")
   type = "text/plain"
  elif "favicon" in req:
   fin=open("favicon.ico","rb")
   type = "image/png"
  else: 
   fin = open("index.html","r")
   type = "text/html"
  content1 = fin.read()
  fin.close()
  
  response = header_gen(type,str(len(content1)))+content1 
  conn.send(response.encode("utf-8")) 
  #conn.close() 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
 s.bind((HOST,PORT))
 s.listen()
 #conn,addr = s.accept() 

 
 t1 = threading.Thread(target=Producer,args=(s,))
 t2 = threading.Thread(target=Consumer,args=())
 t1.start()
 t2.start()
 t1.join()
 t2.join()
 
