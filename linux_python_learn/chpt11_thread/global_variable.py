#! python 
#coding=utf8

import threading
import time



'''
线程间的通讯通过全局变量实现
'''

detail_url_list = []

def get_detail_html(detail_url_list):

    # 模拟爬取页面详情页

    # while 循环保证不停的获取页面信息不关闭线程
    # if 如果初始list为空就跳过
    while True:
        if detail_url_list:    
            print("线程1, 得到html")
            time.sleep(2)
            print("线程1结束")



def get_detail_url(deatail_url_list):
    print("线程2, 得到url")
    time.sleep(4)

    # 爬取20个url信息
    for i in range(20):
        deatail_url_list.append("http://www.baidu.com/{id}".format(id=i))

    print("线程2结束")



if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list, ))

    # 其中10个url被用于获取html页面
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list, ))
        html_thread.start()
        html_thread.join()

    print("主线程结束")


