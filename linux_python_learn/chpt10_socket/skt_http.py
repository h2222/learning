#! python
#coding=utf-8


import socket
from urllib.parse import urlparse


'''
利用socket 建立http请求
'''

def get_url(url):
    url = urlparse(url)
    host = url.netloc 
    path = url.path

    # 如果路径为空, 路径为根路径
    if path == "":
        path = '/'


    # 建立socket 链接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # http 请求, 固定 80端口
    client.connect((host, 80))
    
    # 发送http请求, 固定格式
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n"
                    .format(path, host).encode('utf8'))

    # 初始化接收数据
    data = b""

    # 服务器返回数据接受
    while True:
        d = client.recv(1024) #d为接收数据
        if d: 
            data += d
        else:
            break
    
    # 数据解码并只保留html数据
    data = data.decode('utf8')
    html_data = data.split("\r\n\r\n")[1]
    print(html_data.encode('utf8'))
    client.close()


if __name__ == "__main__":
    get_url("http://www.baidu.com")


