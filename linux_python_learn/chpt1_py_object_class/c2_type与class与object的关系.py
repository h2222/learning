#! python
#coding=utf-8



'''
type与object与class之间的关系
弄明白 python 的继承关系与实例化关系的区别!
具体关系请看 type_object_class_间的关系.png
'''

# 万物起源于type, type()函数用于查看当前对象是被哪个类实例化的
a = 1
b = 'sdc'
# 我们知道 1 是 int的对象, 是class int的实例, 'sdc'的type为 str 对象, 是class int的实例
# 1 是通过 int 这个类 实例化的对象, 'sdc'是通过 str 这个类实例化的对象
print('1',type(1), type(b))


# 那么 int 和 str 的type是什么呢? (int 和 str 是什么类实例化生成的呢?)
# 结果为都为 class 'type' , 所以 type 这类的实例化对象为 int 或 str
print('2', type(int), type(str))


# 在静态语言中, class 也是一个对象
class student():
    pass

# 子类
class xiaoming(student):
    pass

# 类实例化对象
me = xiaoming()

# 可以看到 me 是被 xiaoming类 实例化的
print('3', type(me))
# xiaoming对象(类也是对象) 是被 type类 实例化的
print(type(xiaoming))
# type 对象被自己的类实例化 (c中的指针, 所有类都是type类的实例对象, 连object类(类也是对象)和
# type类 也是 type类的实例对象)
print(type(type))


# 我们在来查看一下继承关系 
# 首先me是object, 是类的实例化对象, 不存在继承类, 所以运行会报错
# print(me.__bases__)
# xiaoming类的父类为student类
print(xiaoming.__bases__)
# student类的父类为object(所有类都继承oject类, type类也不例外)
print(student.__bases__)
# object基类没有父类继承
print('object基类没有父类',object.__bases__)


