# coding = utf-8



'''
unpacking of tuple 

'''

# what happened in a, b = b, a ?
a = 1
b = 2
b, a = a, b

# what is *
t = (2, 8)

# os
import os
path_name, file_name = os.path.split('./love.py')
print(path_name, file_name)

# t = (2, 8) *t = 2 8 unpacking
# declined the *args and **kwargs
print(t, *t)

# the unpacking are not only for tuple but other sequence obj, like list, str
l = [1, 2, 3, 4, 5]
print(l)
print(*l)

# how to use * just for show ?
# the * is good for receive redundan value
a, b, *others = range(5)
print(a, b, others)

# even it can put in middle
a, b, *other, c, d = range(6)
print(a, b, other, c, d)


# named-tuple vs dict
'''
 nameed tuple use less memory than a regular object 
 because they don’t store attributes in a per-instance __dict__.
'''
import collections

# City is name of tuple, other params are name of each fields
City = collections.namedtuple('City', 'name population code')

c1 = City('BJ', '4000', '1000')
print(c1)

# show each fields
print(c1._fields)
# nametuple to order dict
d1 = c1._asdict()
print(d1)
# order dict to dict
print(dict(d1))
