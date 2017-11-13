import socket
import os
import sys
class Client:
    username='N/A'
    def __init__(self):
        self.username=input('用户名:')
        object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('这里是某超高校级的客户端')  # 客户端
        self.connect(object);
    def connect(self,socket):
        flag=True
        while (flag):
            add = input('输入待连接的py服务端...直接输回车表示默认')
            print('输进的是' + add)
            if add == '':
                add = '10.77.2.182'
                print('默认服务端')
            try:
                socket.connect((add, 10888))
            except ConnectionRefusedError:
                cmd = input("无响应，是否继续连接[y/n]")
                if cmd == 'y':
                    continue
                else:
                    exit()
            except TimeoutError:
                print('连接超时...')
                continue
            else:  # print('检查点')
                print('已连接...')
                flag = False
            self.messageTransform(socket)
    def messageTransform (self,socket):
        while True:
            try:
                data = socket.recv(1024)  # 以1024为周期接收
            except ConnectionResetError:
                print('卧槽被服务端拒绝了 Σ(⊙▽⊙\"a')
                os.system('PAUSE')
                os.execl(sys.executable , sys.executable , * sys.argv)
            if data.decode() == '000':
                break
            print('收到回复:' + data.decode())
            detail = input(">>>")
            try:
                socket.send(detail.encode())
            except ConnectionResetError:
                print("连接掉线...")
                exit()
if __name__ == '__main__':
    c=Client()

            # try:
            #     socket.connect((add, 10888))
            # except ConnectionRefusedError:
            #     cmd = input("无响应，是否继续连接[y/n]")
            #     if cmd == 'y':
            #         continue
            #     else:
            #         return False
            # else:
            #     print('检查点')
            #     print('已连接...')
            #     flag = False