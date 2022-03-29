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
   content=codecs.open("bio.txt","r",encoding="utf-8").read()
   type = "text/plain"
   response = header_gen(type,str(len(content)))+content 
   conn.send(response.encode("utf-8")) 
  elif "favicon" in req:
   content=open("favicon.png","rb").read()
   type = "image/png"
   response = header_gen(type,str(len(content))) 
   conn.send(response.encode("utf-8")) 
   conn.send(content)
  else: 
   content = open("index.html","r").read()
   type = "text/html"
   response = header_gen(type,str(len(content)))+content 
   conn.send(response.encode("utf-8")) 
     
   
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
 
