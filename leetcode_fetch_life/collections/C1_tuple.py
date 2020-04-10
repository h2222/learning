# coding = utf-8
import collections


# collections 模块支持的数据结构
print('模块支持的数据结构o', collections.__all__)



# tuple 元组为迭代器
t = iter(i for i in range(1, 20))
t2 = (i for i in range(1, 20))
print(type(t))
print(type(t2))


# tuple 拆包省略
item1, *other = t
print(item1, other)



## tuple 中尽量存放不可变对象, 但是也可对存放可变对象例如list
a = ([1, 2], [2, 3], [3, 4])
a[0].append(3)
print('当tuple中存在可变对象时, 因为可变对象的id没有改变, 所以可以对可变对象进行修改',a)



# list 是可迭代对象, 但不是迭代器对象
# 对象拥有next函数, 为迭代器, 含有 __iter__ 函数, 为可迭代对象 (可迭代对象包含迭代器)
# print(next([1, 2, 3]))






