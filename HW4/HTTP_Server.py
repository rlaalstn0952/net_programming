
from socket import *

s = socket()
s.bind(('',80))
s.listen(10)

mimeType=""
header="HTTP/1.1 200 OK\r\nContent-Type: {}\r\n\r\n".format(mimeType)




while True:
    c , addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    

    if "index.html" in req[0]:

        filename="index.html"
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        
        
        c.send(header.encode())
        
        data = f.read()
        c.send(data.encode('euc-kr'))   
        


    if "iot.png" in req[0]:
        filename = "iot.png"
        f = open(filename,'rb')
        mimeType = 'image/png'
 
        
        c.send(header.encode())

        data = f.read()
        c.send(data)
    
    if "favicon.ico" in req[0]:
        filename = 'favicon.ico'
        f = open(filename,'rb')
        mimeType = 'image/x-icon'
       
        c.send(header.encode())

        data = f.read()
        c.send(data)
        

    if "index.html" not in req[0]:
        

        error="HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>"
        
        c.send(error.encode())

    
   
    c.close()
    