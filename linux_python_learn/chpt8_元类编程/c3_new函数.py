#! python
# coding = utf-8


'''
__new__ 和 __init__的区别


new 初始化 类对象
init 初始化 类实例化对象
'''


class Student:

    def __init__(self, string):
        self.string = string
        

    def __new__(cls, string):
        print('this is new')
        


if __name__ == "__main__":
    s1 = Student('this is init')
    
    print(s1.string)
    
       


