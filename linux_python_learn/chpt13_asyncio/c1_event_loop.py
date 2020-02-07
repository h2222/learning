#! python
# coding = utf-8

import asyncio
import time
from functools import partial # 偏函数, 可以在函数中额外添加参数 

'''
asyncio 的使用, 事件循环, 单线程并发

偏函数, 协程返回值, callback函数

asyncio.wait 和 asyncio.gather 的区别
'''

# 协程
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return "this is return result"


# callback函数, 在发生异常时执行的函数
# 本次定义为发生异常给boddy发送邮件
# 如果希望对callback传参, p放在前面
def callback(p, future):
    print(p)
    print("send email to boddy")



if __name__ == "__main__":
    start = time.time()
    
    # 定义事件循环(一个事件(线程)只有一个loop)
    loop = asyncio.get_event_loop()
    # 并发任务, 获取10次html
    tasks = [get_html("http://baidu.com") for i in range(10)]
    
    # 开始执行协程, wait函数为等所有协程执行结束
    loop.run_until_complete(asyncio.wait(tasks))

    # 可以看到所有10条html执行完毕后, 用时为2秒不是20秒, 说明程序并发执行在不同的协程中
    print(time.time() - start)

    ##################################################################
    # 协程的返回值处理
    start = time.time()
    loop2 = asyncio.get_event_loop()
    # 使用loop2.create_task创建返回协程返回值
    task = loop2.create_task(get_html("http://www.baidu.com"))
    # 在结束时值call, back, 如果希望在callback内传入参数, 使用偏函数
    # partial
    task.add_done_callback(partial(callback, "this is a param"))
    loop.run_until_complete(task)
    print(task.result())

    #####################################################################
    # gather 和 wait的区别
    # gather 更加的high level
    # gather 可以做到对协程的分组
    group1 = [get_html("http://www.baidu.com") for i in range(2)]
    group2 = [get_html("http://www.google.com") for i in range(2)]

    # *代表将group参数化, 类似于*args
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)

    # 批次取消任务
    group2.cancel()

    # 批量执行并发任务
    loop.run_until_complete(asyncio.gather(group1, group2))





