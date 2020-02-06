#! python
#coding=utf-8

import socket

def client_1():
    # socket 客户端部分
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 1. 建立连接
    client.connect(('127.0.0.1', 8000))
    client.send("这是来自客户端的请求".encode('utf-8'))
    client.close()


'''
利用socket 服务器实现 客户端和服务器的聊天
'''
def client_chat():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8000))


    # 实现聊天
    while True:
        # 发送 
        s_data = input()
        client.send(s_data.encode('utf-8'))

        # 接受
        data = client.recv(1024)
        print(data.decode('utf-8'))
    else:
        client.close()


if __name__ == "__main__":
    client_chat()