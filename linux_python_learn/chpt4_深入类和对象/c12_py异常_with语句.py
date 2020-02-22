#! python 
# coding= utf-8

import contextlib

'''
了解 try raise except finally
了解 上限文管理器协议, 了解python协议与魔法函数间的关系, 了解 with
了解 上下文管理器的生成器实现, contextlib

'''



def except_test():
    try:
        print('start test')
        raise KeyError  # raise 举起, 抛出, 人为定义直接抛出某个异常
    except KeyError as e:   # except 接收某个异常
        return '返回错误1 \n'
    else:    # try 后可以接else, 代表如果没有捕获到特定异常或没有捕获的到异常, 执行else内容
        return '返回其他错误或正常运行'
    finally:
        pass
        # return 'end test'

# 上下文管理器协议
#  协议认为: 如果一个类实现了 enter 和 exit 函数, 即认为该类遵循上下文管理器协议
#  即可以使用 with 关键字进行山下文管理

class Student:

    # __enter__函数, 类对象实例化时执行, 用于数据的导入
    def __enter__(self):
        print("enter")
        return self

    # 普通实例化对象函数    
    def do_something(self):
        print("doing something")

    # __exit__ 在执行完所有对象操作时执行, 用于数据的释放及异常抛出
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit \n")


# 使用生成器遵循上下文管理器协议
@contextlib.contextmanager
def file_open(file):
    print("start file")
    yield {}
    print("end file")

if __name__ == "__main__":


    # 异常返回顺序问题, 当在执行try中遇到异常并在except准备return时, return的内容会被堆栈至栈帧中
    # 程序继承执行, 当发现finally下包含return时, 将finally中return的内容堆入栈帧, 最后返回栈帧的最上层
    # 即finally中的return内容, 如果想返回except中的return内容需要将finally下的return注释掉    
    print(except_test())

    # 测试 with 
    with Student() as s:
        s.do_something()

    # 测试生成器 with
    with file_open("a file") as f:
        print('file preprocessing')