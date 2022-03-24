from socket import *


sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',3333))
sock.listen(2)
print("waiting....")
cal_new =[]
table =["+","-","*","/"]
while True:
    client, addr = sock.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
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
