from socket import *
import random
import time

BUF_SIZE =1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(10)
print("Device start")

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

    
    Heart, Steps, Cal = random.randint(0,40) , random.randint(0,100), random.randint(70,150)

    data = '{}: Device2:  Heartbeat={}, Steps={}, Cal={}\n'.format(time.ctime(),Heart,Steps,Cal)
    conn.sendall(data.encode())

    msg = conn.recv(BUF_SIZE)
    if not msg:
        pass
    else:
        print("clent:", addr, msg.decode())

    # f.close()
    conn.close()