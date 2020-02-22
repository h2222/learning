#! python
# coding = utf-8


'''
集合 set
1. set 中的元素不重复, 无序, 一般用于序列去重
2. set 为集合类型, 与序列类型的方法不通用
3. set 和 dict 的实现为 hash算法(散列链表), 时间复杂度O(1), 性能高于list
4. 集合类型包含 set, forzen set, 其中 冻结set不同被修改, 通常用于dict的key
'''


# set 的去重特性
sf1 = frozenset('dadasdasdasdasdasd')
s1 = set('aaaaffffhhhhsssscvvvwwwghhhqqqfghh')
print(s1, '\n') # 随机排序且不重复



# 向set数据操作(符号 -, |, &)
another_set = set('xyz')

# 求并集
cor_s = s1 | another_set
print('交集:', cor_s, '\n')

# 交集
bin_s = s1 & another_set
print('并集:', bin_s, '\n')

# 减
sub_s = s1 - another_set
print('相减:', sub_s, '\n')

# 加
s1.add('x')
print('相加', s1, '\n')

# 判断子集
x = set('qq')
print(x.issubset(s1), '\n')







