#! python
#coding=utf-8

'''
socket 编程流程



1. 应用层(http, ftp, ...) 分别对应不同的服务器
2. 传输层 (端对端的接口, 端口, 端是指不同的服务器)即为不同的服务器分配一个独立的号码

          服务器 (server)                                         客户端(client)
                                                                       
socket (此步骤为 bind协议, 地址, 端口)                                socket
|                                                                      |
listen(监听客户端发送的请求)                                            |
|                                                                      |
调用accept函数, 直到客户端client发送了连接请求                           |
|                                                                      |
阻塞等待请求<---------------------TCP三次握手------------------------- connect() 连接请求(仅仅只是连接请求)
|                                                                       |
receiver(接受来自客户端的数据)<--------------------------------------- send() (客户端发送数据)
|                                                                       |
send()(服务器将响应数据发送回客户端) ---------------------------------> receiver(客户端接受服务器的响应数据)
|                                                                        |
close() 服务器关闭, 流程结束<----------------------------------------- close() (客户端请求关闭)

'''

import socket
import threading



'''
客户端单向发送请求给socket服务器
'''
def server_1():
    # 实现 socket 服务器和客户端的demo

    #1. 建立服务器
    # AF_INET 指 ipv4 网络服务器, AF_INET6 为ipv6 网络服务器
    #SOCK_STREAM 指遵循TCP协议, SOCK_UDP 指遵循UDP协议
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定地址端口 bind
    # 必须为tuple类型, 端口为8000
    server.bind(('0.0.0.0', 8000))

    #3.服务器监听客户端请求, 获取独立的sock 和 客户端地址
    server.listen()
    sock, addr = server.accept()

    #4. 接收来自客户端的数据, 每次接收1024字节的数据, 即1kb
    data = sock.recv(1024)
    # 解码格式为utf-8
    print(data.decode("utf-8"))

    # sock关闭, 服务器关闭
    sock.close()
    server.close()


'''
利用socket 服务器实现 客户端和服务器的聊天
'''
def server_chat():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8000))
    server.listen()
    sock, addr = server.accept()

    # 实现聊天
    while True:
        # 接受
        data = sock.recv(1024)
        print(data.decode('utf-8'))

        # 发送 
        s_data = input()
        sock.send(s_data.encode('utf-8'))
    else:
        sock.close()
        server.close()



'''
利用socket 服务器和多线程技术, 实现多个客户端和服务器的聊天
'''

def handle_sock():
    while True:
        # 接受
        data = sock.recv(1024)
        print(data.decode('utf-8'))

        # 发送 
        s_data = input()
        sock.send(s_data.encode('utf-8'))

def server_chats():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8000))
    server.listen()

    # 实现聊天
    while True:
        # 监听会有多个用户请求连接 server, 说sock 写在while循环内, 每次与新的client就创建一个新的sock
        sock, addr = server.accept()
        # 利用线程实现多客户端处理
        client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
        client_thread.start()
    else:
        sock.close()
        server.close()

        


if __name__ == "__main__":
    server_chats()
