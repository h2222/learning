# coding=utf-8





'''
defaultedict

1. C语言实现, 性能好
2. missing 实现
'''


from collections import defaultdict

# 对字典进行初始化操作


# defaultdict 传入的是可调用对象(例如函数)
dd = defaultdict(int)
l = ['n1', 'n2']
for i in l:
    print(dd[i])


# 函数为可调用对象时
value = lambda : 'value'
dd2 = defaultdict(value)
for i in l:
    print(dd2[i])
