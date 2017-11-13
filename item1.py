import socket
def judge(a):
	if(a=="苟利国家生死以"): return "岂因祸福避趋之"
	return a

print('这里是欧拉欧拉欧拉服务器...')#服务端
a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

a.bind(('',10888))#input(输入待连接的端口号...)))
a.listen(1)

b,c=a.accept()
print ("\a")
print('已连接至:'+str(c))
data='这里是欧拉欧拉欧拉欧拉服务器！'.encode()
b.send(data)
while True:
    try:
        data=b.recv(1024)
        data_ = ''.encode()
        b.send(data_ + data)
        print('消息回馈已发出...')
    except ConnectionResetError:
        print('客户端掉线')
        print("客户端接收:" + data.decode() + '..')
        data = judge(data.decode()).encode()
    if data.decode()=='000':
        print('消息接收过期，即将退出...')
        break
b.send('assassin'.encode())
print('服务器已关闭')
a.close()
