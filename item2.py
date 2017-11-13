import socket
import os
def Exit():
    print('按任意键以关闭客户端..')
    os.system('PAUSE')
    a.close()
a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
flag=True
print('这里是某超高校级的客户端')#客户端
while (flag):
    add = input('输入待连接的py服务端...直接输回车表示默认:')
    print('输进的是',end='')
    if add == '':
        add = '10.77.2.182'
        print('默认服务端')
    else:print()
    try:
        a.connect((add, 10888))
    except ConnectionRefusedError:
        cmd = input("无响应，是否继续连接[y/n]")
        if cmd == 'y':  continue
        else:   Exit()
    except TimeoutError:
        print('连接超时...')
        continue
    else:   #print('检查点')
        print('已连接...')
        flag = False
while True:
    data=a.recv(1024)#以1024为周期接收
    if data.decode()=='000':break
    print('服务端回复:'+data.decode())
    detail=input(">>>>>>")
    try:a.send(detail.encode())
    except ConnectionResetError:
        print("连接掉线...")
        Exit()