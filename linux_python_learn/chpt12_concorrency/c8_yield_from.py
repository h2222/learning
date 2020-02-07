#! python
# coding = utf8 

from itertools import chain



'''
理解yield from

'''

my_list = [1, 2, 3]
my_dict = {"b1":"s11111", "b2":"s2222222", "b3":"s3333333"}


# 利用 chain 函数将三个可迭代对象合并为使用一个for循环就能完成 

for value in chain(my_list, my_dict, range(7, 10)):
    print(value)


# 利用 yield 实现生成器版本低合并chain
# *args 会传递一个 list, list中的元素时不确定的, 一种写法时可以用作for循环对象

def my_chain(*args, **kwargs):
    # 从list拿到每一个可迭代对象
    for my_iterable in args:
        # 从可迭代对象中拿出元素
        for value in my_iterable:
            # 最后使用生成器的方式返回
            yield value 

c1 = my_chain(my_list, my_dict, range(7, 10))

print('测试哈自己的生成器')
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
