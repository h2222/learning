#! python
# coding = utf-8


'''
+ , += , extend, append 之间的区别

'''


a = [1, 2]

# 在list后接+ 号表示直接在后面添加, 但只能添加与当前list类型相同的类型
b = a + [3, 4]



# += 的实现起始是调用的list类中的extend函数
# a.extend((3, 4)) 因为extend(iterable) 只要是iterable类型的参数都行
# 所以 += 可以添加与a不相同的类型的可迭代类型(例如元组)
a2 += (3, 4)


# extend 函数, 在list类型后面继续添加
# [1, 2, 3, 4]
a.extend(([3, 4])

# append 函数, 将参数正态作为一个元素添加到 list中
# [1, 2, [3, 4]]
a.append([3, 4])








