#! python
# coding=utf-8



'''
类变量 与 实例变量

在python中, 万事万物皆对象

所以类对象有自己的变量, 类的实例化对象也有自己变量

类对象直接写在类下面, 实例化对象的变量写在__init__函数中

'''

class Student:
    # 类变量
    name = 'hao'
    age = 18

    # 类实例化对象的变量
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.level = 3


if __name__ == "__main__":

    # s1 为类的实例化对象, Student为类对象
    s1 = Student('hao','high school')

    print('1', s1.level) # 1.类实例化对象独有的变量
    print('2', Student.age) # 2.类对象独有的变量(在编译类时就会被声明)
    print('3', s1.name, s1.age) # 3.python的自下而上的变量寻找机制, 如果在类实例化对象找到了变量就使用实例化的变量, 如果没有找到就去类变量里找

    # 类变量和实例变量都可以在运行时 添加 或 修改
    Student.age = 25
    Student.No = 10086
    s1.name = 'wang'

    # 但是类变量可以永久保存, 但实例化变量却会在重新实例化时被初始化
    s2 = Student('hao', 'high school')
    print('4', Student.No, s2.name)




    
