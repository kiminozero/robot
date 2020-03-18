# coding=utf-8
import sys
import socket
import threading
 
#打开server端口，listen,处理传进来的数据
def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind(local_host,local_port)
    except:
        print('[!!] Failed to listen on %s:%d'%(local_host,local_port))
        print('[!!] Check for other listening sockets or correct permissions')
        sys.exit(0)
    print('[*] Listening on %s:%d'%(local_host,local_port))
    server.listen(5)
    while True():
        client_socket,addr = server.accept()
        print('[==>] Received incoming connection from %s:%d'%(addr[0],addr[1]))
        proxy_thread = threading.Thread(target = proxy_handler,args = (client_socket,remote_host,remote_port,receive_first))
        proxy_thread.start()
 
#这个函数定义了代理服务器的主要处理方法
def proxy_handler(client_socket,remote_host,remote_port,receive_first):
    #连接上远程主机
    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    remote_socket.connect((remote_host,remote_port))
    #如果receive_first为true说明要先从远程主机接收数据
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        #看一看远程主机过来的内容有没有想要的东西^_^偷窥下
        hexdump(remote_buffer)
        #将接收到的数据处理下
        remote_buffer = response_handler(remote_buffer)
        #remote_buffer处理过后长度不为0说明要把数据传给客户端
        if len(remote_buffer):
            print('[<==] Sending %d bytes to local_host.'%len(remote_buffer))
            client_socket.send(remote_buffer)
    #不断地接收来自远程主机和客户端的信息然后发送给对方
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print('[==>] Received %d bites from local_host.'%len(local_buffer))
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print('[==>] Sent to remote')
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print('[<==] Received %d bytes from remote.'%len(remote_buffer))
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print('[<== Sent to local_host]')
        #两边都没有数据，关闭连接，我怀疑这里会出问题
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_buffer.close()
            print('[*] No more data. Closing connections.')
             
            break
 
#这个函数不大懂意思，后面仔细研究下
def hexdump(src,length = 16):
    result = []
    digits = 4 if isinstance(src,unincode) else 2 #我的理解是中文4，外文2
    #xrange不会直接生成list，而是生成一个对象，要用的时候再去调用对象里面的东西
    for i in xrange(0,len(src),length):
        s = src[i:i+length]
        hexa = b' '.join(['%0*x'%(digits,ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) <= 0x7F else b'.' for x in s])
        result.append(b'%04X  %-*s  %s'%(i,length*(digits + 1),hexa,text))
    print(b'\n'.join(result))
 
def receive_from(connection):
    buffer = ''
    #设置两秒超时
    connection.settimeout(2)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer
 
#定义远程和本地主机消息处理函数，这里没有需要，不做操作
def request_handler(buffer):
    return(buffer)
def response_handler(buffer):
    return(buffer)
         
def main():
    #从命令行读入参数，如果数目不对则报错
    if len(sys.argv[1:])!= 5:
        print('Usage: python tcp_proxy.py [local_host] [local_port] [remote_host] [remote_port] [receive_first]')
        print('Example: python tcp_proxy.py 127.0.0.1')
        sys.exit(0)
     
    #设置监听参数
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
     
    #设置远程目标
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
     
    #告诉代理在发送数据前接收连接和接收数据，不大懂，先存疑
    receive_first = sys.argv[5]
    if 'True' in receive_first:
        receive_first = True
    else:
        receive_first = False
    #开始监听，然后代理开始工作！
    server_loop(local_host,local_port,remote_host,remote_port,receive_first)
 
main()