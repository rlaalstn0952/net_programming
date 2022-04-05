from socket import *
import random

port =5555
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('',port))
box = {}


while True:
    data,addr = sock.recvfrom(BUFFSIZE)
    data = data.decode().split(' ')
    mode, num = data.pop(0), data.pop(0)
    

    print(mode, num)
    
    if num not in box:
        box[num] = []

    if(mode =='send'):
        message = ' '.join(data)
        box[num].append(message)
        resp="OK."
        

    if(mode =='receive'):
        
        if box[num] ==[]:
            resp ="No messages"
        else:
            resp = box[num].pop(0)
    
    if(mode =='quit'):
        break
    sock.sendto(resp.encode(), addr)