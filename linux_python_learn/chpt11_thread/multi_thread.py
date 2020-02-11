#! python
#coding=utf8
import time
import threading


'''
使用threading模组完成python的多线程编程
'''

def get_detail_html(url):
    print("线程1, 得到html信息")
    time.sleep(2) # 线程sleep 2s
    print("线程1结束")


def get_detail_url(url):
    print("线程2, 得到url信息")
    time.sleep(2) # 线程sleep 2s
    print("线程2结束")



# 多线程实现方式2, 继承threading.Thread类
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        # super调用父类init方法, 直接命名线程名称
        super().__init__(name=name)
    
    def run(self):
        print("线程3, 得到html信息")
        time.sleep(2) # 线程sleep 2s
        print("线程3结束")


class GetDetailURL(threading.Thread):
    def __init__(self, name):
        # super调用父类init方法, 直接命名线程名称
        super().__init__(name=name)
    
    def run(self):
        print("线程4, 得到url信息")
        time.sleep(2) # 线程sleep 2s
        print("线程4结束")
        

# mian 为主线程
if __name__ == "__main__":
    # 创建线程, target为线程具体执行函数 args为线程函数的参数
    thread1 = threading.Thread(target=get_detail_html,args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    thread3 = GetDetailHtml('线程3')
    thread4 = GetDetailURL('线程4')



    # 守护线程( 当主线程main结束时, 守护线程一定结束)
    thread1.setDaemon(True)
    thread2.setDaemon(True)

    # 计时, 线程启动
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    # join函数, 必须等其他线程运行结束主线程才能结束
    # 和守护线程相反
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("主线程结束, 用时:", time.time() - start_time)
