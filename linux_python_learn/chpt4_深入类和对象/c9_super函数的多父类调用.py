#! python
# coding = utf-8



'''
super 函数为调用父类方法
'''



class A:
    def __init__(self):
        print('A类实例的init方法')


class B(A):
    def __init__(self):
        print('B类实例的init方法')
        super().__init__()

class C(A):
    def __init__(self):
        print('C类实例的init方法')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('D类实例的init方法')
        super().__init__()


if __name__ == "__main__":
    # 如果使用super方法调用父类方法, 安装BFS顺序调用
    d = D()
