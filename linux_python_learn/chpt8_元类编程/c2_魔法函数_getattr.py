#! python
# coding = utf-8




'''
__getattr__
__grtattribute__

如果对象中传入的参数是序列类型或映射类型, 说明一个参数内又包含了其他参数, 我们怎样才能将序列内的参数获取呢?
'''


class Student:
    def __init__(self, info):
        self.info = info

    def __getattr__(self, key):
        return self.info[key]

    #  __getattribute__ 的作用为, 当__getattr__找不到变量时, 会报错
    # 但是如果有 __getattribute__, 对象会直接来着找, 连info理都不理
    def __getattribute__(self, item):
    def __getattribute__(self, item):
        return 'hao jiaxiang'

if __name__ == "__main__":
    s1 =  Student({'name':'hao', 'age':'18', 'level':'3'})
    
    # 在对象声参数声明中, 我们并没有name变量, 但name变量存在于info参数中, 所以可以使用
    # __getattr__去对字典参数寻找name参数
    print('student\'s name is ', s1.name)