#! python
# coding = utf-8

import array
import bisect
'''
为什么我们用array(数组)替代list(列表)
python的序列类型:   list   tuple    bytes   range   str     array
python的集合类型:   set     
python的映射类型:   dict

1. array是以连续的内存空间存储在内存中的(java中的数组)
'''

# 参数代表在array中的类型, i - singed integer 带符号常数
my_array = array.array('i')


my_array.append(1)
my_array.append(2)

bisect.insort(my_array, 3)

print(my_array[:2])