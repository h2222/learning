#! python
#coding=utf-8



'''
python 中的多态, 鸭子法则

怎样判断一个动物是不是一只鸟?
如果这个动物它能飞, 我们就说该动物是一只鸟

python是动态语言, 动态语言是没有变量类型的,  python中的变量只是一个符号, 是一个可以指向任何类型的对象
动态语言的缺陷: python在编译时难以检查错误,  像java在编译时还会有下划线提醒变量类型错误, python只有在运行时
才能知道是否错误
所以没有真正意义上的多态, 但是可以通过定义相同名称的类函数实现多态

!!!
在java中, 我们有不同的类型, 你定义什么类, 就有什么样的类型, 例如你定义了
Student 类, 就有 Student 这种类型 Student s1 = Student(), 在或者基本数据类型
也是由类定义的 int a = Integer()
但在python中, 动态语言不会强制性的要求数据是什么类型, 所以python中的基本类型
其实就是  普通的类遵循了某种协议(或者说的直白一点, 实现了某种魔法函数)  就成了某种类型
举个例子, 如果Student这个类时 str 类型, 那Student类必定实现了__str__魔法函数, 这就是字符串协议
如果Student类实现了 __iter__或__len__函数, 那Student类就是list类型

'''


# 定义了三个动物的类, 他们都有共同的函数, fly
class Animal1(object):
    def fly(self):
        print("Animal1 can fly")

class Animal2(object):
    def fly(self):
        print("Animal2 can fly")

class Animal3(object):
    def fly(self):
        print("Animal3 can fly")

if __name__ == "__main__":
    a1 = Animal1()
    a2 = Animal2()
    a3 = Animal3()

    # python的'多态', 同一个函数名但不同的功能
    for a in [a1, a2, a3]:
        print(a.fly())    