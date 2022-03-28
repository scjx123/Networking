import socket 
import codecs
HOST = "0.0.0.0"
PORT = 9999
def header_gen(type,len):
 return "HTTP/1.1 200 OK\r\n Connection: close\r\n Content-Type: {}\r\n Content-Length: {}\r\n\r\n".format(type,len) 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
 s.bind((HOST,PORT))
 s.listen()
 #conn,addr = s.accept() 
 while True:
  conn,addr = s.accept()
  type = ""
  req = conn.recv(1024).decode()
  print(req)
  if "bio.txt" in req:
   fin=codecs.open("bio.txt","r",encoding="utf-8")
   type = "text/plain"
  elif "favicon" in req:
   fin=open("favicon.png")
   type = "image/png"
  else: 
   fin = open("index.html","r",encoding="utf-8")
   type = "text/html"
  content1 = fin.read()
  fin.close()
  
  response = header_gen("text/html",str(len(content1)))+content1 
  conn.send(response.encode("utf-8")) 

  #send http response 
  #response = "HTTP/1.0 200 OK\n\n"+ content1
  #conn.sendall(response.encode())
  conn.close() 


