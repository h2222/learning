#! python
# coding=utf-8


'''
数据封装与私有变量

实际上, python的私有属性并不知道真正意义上的私有, 只是把内部变量名改了


self.__a = 1   -->   a1.__class_a

'''


class Student:
    __school = 'high school'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name():
        return self.__name
    
    def set_name(name):
        self.__name = name
    

if __name__ == "__main__":
    s1 = Student('hao', 18)

    # python 将私有属性有 __name 转换为 _school__name, 实现了属性私有, 规范写法
    print(s1._Student__name)
    # 类属性私有
    print(Student._Student__school)
