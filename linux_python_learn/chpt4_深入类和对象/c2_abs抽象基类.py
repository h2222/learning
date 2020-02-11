#! python 
# coding=utf-8
from collections.abc import Sized  # 从抽象基类中引入Sized的类型, 就是能数的那种类型
import abc # abc 抽象类

'''
抽闲基类, 就是python的 接口类型, 因为没有变量类型限制, 抽象基类的定义全凭自觉, 就是所谓的遵守协议

java中的接口中的方法(函数)是不能实现的, python中的也是, 使用pass代替
'''


# 抽象基类的用法1: 判断某个对象的类型(实现__len__使类对象变为Sized类型)
class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    # 实现__len__函数后, 类实例化对象可以调用len()函数, 并且对象同时也是Sized的实例(因为python承认多继承)    
    def __len__(self):
        return len(self.employee_list)

# 抽象基类的用法1: 指定框架, 强制开发者在继承该类时必须实现某些方法(java中的接口)
# 在继承Student类时, 必须实现school和homework函数
class Student(object):
    def school(self, name):
        pass
    def homework(self, name, subject):
        pass

# 抽象基类的标准表达
class Student2(metaclass=abc.ABCMeta):
    # 使用abc.xxx 修饰器来修饰抽象基类
    @abc.abstractclassmethod
    def school(self, name):
        pass
    @abc.abstractclassmethod
    def homework(self, name, subject):
        pass



if __name__ == "__main__":
    c1 = Company(['hao', 'wang', 'zhang'])

    # 可以看到 c1 也是 Sized的实例
    print(isinstance(c1, Sized))
    # 同时我们也可以看到c1中实现了__len__的属性, (函数也是一种属性, 在python中)
    print(hasattr(c1, "__len__"))

