from socket import *
import random
import time
port =3333
BUFFSIZE = 1024


c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost',port))


while True:
    reRx = 0
    msg = input('-> ')
    while reRx <= 3:
        resp = str(reRx) + ' ' + msg
        
        c_sock.send(resp.encode())
        c_sock.settimeout(2)
        

        try:
            data = c_sock.recv(BUFFSIZE)
            if(data.decode() == 'ack'):
                break
            
        except timeout:
            reRx += 1
            
            continue
        else:   
            break
        
    else:
        print("reRx > 3 , break")
        
        break

    while True:
        c_sock.settimeout(None)
        data = c_sock.recv(BUFFSIZE)
        if random.random() <=0.5:
            continue
        else:
            c_sock.send(b'ack')
            print('<-',data.decode())
            break
            

