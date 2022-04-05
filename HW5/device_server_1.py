from socket import *

import random
import time

BUF_SIZE =1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print("Device 1 start")

while True:
    conn, addr = sock.accept()

    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg != b'Request':
        print('client:', addr, msg.decode())
        conn.close()
        break
    else:
        print('client:', addr, msg.decode())
    

    

    filename = "data.txt"
    print('client:', addr, filename)

   
    Temp, Humid, lilum = random.randint(0,40) , random.randint(0,100), random.randint(70,150)
    data = '{}: Device1:  Temp={}, Humid={}, lilum={}\n'.format(time.ctime(),Temp,Humid,lilum)
    conn.sendall(data.encode())

    msg = conn.recv(BUF_SIZE)
    if not msg:
        pass
    else:
        print("clent:", addr, msg.decode())

    
    conn.close()