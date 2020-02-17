#! python
# coding = utf-8


'''
方法参数化,   property 
一般用于op类, getter setter
'''


class Student:
    
    # 在op类中, 我们不希望内部属性对外暴露, 所以需要使用getter和setter
    def __init__(self, name, age, level):
        self.__name = name
        self.__age = age
        self.__level = level

    # 传统getter和setter非常笨重, 没调用必须使用调用方法, 例如 obj.getter()
    # 现在, 我们使用@property装饰器对getter和setter进行装饰, 时在调用是可以直接将函数作为属性进行调用
    # 例如: obj.age 或者 obj.age = 18
    @property
    def age(self):
        return self.__age
    
    # 同时, 在使用obj.setter对setter方法进行属性化的时候, 可以对属性进行修改
    @age.setter
    def age(self, age):
        age += 1
        self.__age = age
    
    # 同时, @property也可以之间将函数作为类实例化对象的可读属性(注意, 只能读取,不能修改)
    # 例如在本类中, level_name是不存在的属性, 但通过property我们可以得到
    @property
    def level_name(self):
        return str(self.__level) + '_' + str(self.__name)




if __name__ == "__main__":
    s1 = Student('hao', 25, 3)

    # 测试age 获取与设置
    print('age:', s1.age, '\n')
    s1.age = 26
    print('age:', s1.age, '\n')
    

    # 测试初始化私有属性(不是通过属性化方法调用)
    print('age (private):', s1._Student__age)

    # 测试只读属性
    print('read only level_name:', s1.level_name)
