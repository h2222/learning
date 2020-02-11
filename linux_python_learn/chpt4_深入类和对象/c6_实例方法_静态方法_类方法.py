#! python
# coding=utf-8



'''
深刻理解 实例方法,  静态方法, 类方法 

实例方法: 类实例化对象可以调用的方法, 同城定义为 def a(self, ...) 其中self 指的就是类实例的对象
静态方法: 不需要实类例化对象也可以引用的方法,就是普通方法放在类内, 通常加修饰器@staticmethod
类方法: 不需要实例化对象也可以引用的方法, 与静态方法有略微不同, 同城加修饰器@classmethod

'''



class Date:
    # 类变量
    date = '这个一个测试类方法的函数'

    # 初始化实例函数__init__
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # 实例方法
    def add_1(self):
        self.day += 1

    #静态方法, 不用实现实例对象, 所以不用添加self
    @staticmethod
    def isSunDay(week):
        if week == 'sunday':
            return True
        else:
            return False
    
    # 类方法, 也不需要实例化对象, 但如果在函数中需要调用类变量或需要类实例化
    # 时, 类方法就是不二之选, 通常选择cls参数代表Data的类对象
    @classmethod
    def init_in_str(cls, s):
        print(cls.date)
        year, month, day = s.split("-")
        return cls(year, month, day)


if __name__ == "__main__":
    d1 = Date('2020', '2', '11')    
    # 在实例对象d1调用add_1方法时, python会自动的将
    # add_1(self) 转换为 add_1(d1), 所以所以实例函数必须加参数self
    d1.add_1

    # 测试静态方法
    print(Date.isSunDay('sunday'))

    #测试类方法
    d2 = Date.init_in_str('2020-2-11')
