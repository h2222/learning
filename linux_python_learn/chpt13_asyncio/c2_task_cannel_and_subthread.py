#! python
# coding = utf-8

import asyncio
import time



'''
task 的取消 与 子进程 的调用
'''


# 协程
async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)
    print("done after {}s".format(sleep_times))


if __name__ == "__main__":
    # 模拟任务执行时间
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(4)

    # 并发执行
    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()

    # 当一个任务失败后(模拟使用 ctrl+c 模拟task失败), 终止所有任务, 打印信息
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cannel task!")
            print(task.cancel())
        # 事件循环停止
        loop.stop()
        loop.run_forever()
    finally:
        # 关闭事件循环
        loop.close()

