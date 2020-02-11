#! python
#coding=utf-8

'''
了解认识魔法函数

1. 魔法函数可以在任何类中使用
2. 类在实例化时, 魔法函数字典执行不需要调用
3. 魔法函数 双下划线开始, 双下划线结束 __init__
'''


class students(object):
    def __init__(self, name_list):
        self.name = name_list


    # str 魔法函数
    def __str__(self):
        return ','.join(self.name)

    # repr 魔法函数, 之前你得打印一下才能出触发__str__函数
    # repr 直接连打印都不用了, s1直接返回字符串类型
    def __repr__(self):
        return ','.join(self.name)

# 测试
if __name__ == "__main__":
    # 通常情况下, s1 返回的应该为 class 类对象 object 类
    # 但是有 __str__或 __repr__ 的情况下, s1 被允许转换为 字符串 类型
    s1 = students(['hao', 'li', 'wang'])
    
    # print(s1)