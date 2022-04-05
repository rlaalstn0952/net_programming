from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4



while True:
    num = input("Enter num: ")
    if(num == '1'):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 7777))
        s.send(b'Request')

       
        filename="data.txt"
        f = open(filename, 'a')
        data = s.recv(BUF_SIZE)
   
        f.write(data.decode())
        f.close()
        s.close()
        
    elif (num== '2'):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 8888))
        s.send(b'Request')

       
        filename="data.txt"
        f = open(filename, 'a')
        data = s.recv(BUF_SIZE)
   
        f.write(data.decode())
        f.close()
        s.close()
        
    else: 
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 7777))
        s.send(b'quit')
        s.close()


        v = socket(AF_INET, SOCK_STREAM)
        v.connect(('localhost', 8888))
        v.send(b'quit')
        v.close()