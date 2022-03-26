import MyTCPServer as my

port =3333
BUFSIZE=1024
sock = my.TCPServer(port)
client,addr = sock.Accept()
print('connection from ', addr)
cal_new =[]
table =["+","-","*","/"]
while True:
    
    
    while True:
        data = client.recv(BUFSIZE)
        if not data:
            break

        try:
            cal = data.decode() # byte를 문자열로
            for table in cal:
                if table == '+':
                    cal = cal.split('+')
                    cal = int(cal[0]) + int(cal[1])
                elif table == '-':
                    cal = cal.split('-')
                    cal = int(cal[0]) - int(cal[1])
                elif table == '*':
                    cal = cal.split("*")
                    cal = int(cal[0]) * int(cal[1])
                elif table == '/':
                    cal = cal.split('/')
                    cal = float(cal[0]) / float(cal[1])
                    cal = round (cal, 1)
            cal = str(cal)
            
        except:
            client.send(b'Try again')
        else:
            
            client.send(cal.encode())
    client.close()
