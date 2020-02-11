#! python
# coding=utf-8




'''
isinstance 和 type 的区别

isinstance(a, b) 是指a是否为b的实例的对象
type(a) 是指a的对象

在python中, 所以东西都是对象!!!
所以在继承关系中, 对象是子类的实例化的对象, 子类继承父类, 所以对象也是父类的实例化对象
但是 父类的对象 和 子类的实例化的对象是两个完全不同的对象, 注意, 这里没有说的是父类对象, 不是父类实例化的对象(因为在python,万物皆对象, 类也是对象)
所以 type 和 instance 可能返回的结果是不同的
'''

class A():
    pass

class B(A):
    pass

# b 是B类实例化的对象
# b 也是A类实例化的对象
b = B()
print(isinstance(b, B), isinstance(b, A))

# A为父类的对象, A与b不相同
# 所以, 以后请谨慎使用type, 多使用isinstance
print(type(b) is A)