#! python
# coding = utf-8


'''
切片进阶: 通过切片去修改值或添加值
'''

a = [i for i in range(1, 20, 2)]

print(a, '\n')

# 切片翻转
print(a[::-1], '\n')


# 当切片起始位置大于列表长度时, 可以在尾部添加元素
a[len(a):] = [-99]
print(a, '\n')


# 当切片终止位置小于列表长度时, 可以在头部添加元素
a[:0] = [-99]
print(a, '\n')

# 可以切片前后元素相同时, 表示切片在元素的缝隙中, 可以在两元素缝隙间插入元素
a[3:3] = ['insert']
print(a, '\n')


# 切片其实是主list的sub_list, sub_list可以被替换, 达到替换list中某些元素的目的
# 其中 sub_list的长度必须与替换list的长度相同, 不然会报错
a[:3] = ['0', '1', '2']
print(a, '\n')


# 隔x个取一个组成一个sub_list, 然后把sub_list换成其他的
a[::4] = ['j1', 'j2',  'j3', 'j4']
print(a, '\n')


# 秀, 其中[x] * n  --> [x, x, x, x, ...]  长度为n
a[::4] = ['秀'] * len(a[::4])
print(a, '\n')


# 删除前3个元素
a[:3] = []
print(a, '\n')

# 删除整个列表
del a[:len(a)]
print(a)












































