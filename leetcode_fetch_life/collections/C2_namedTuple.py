# coding = utf-8




'''
namedtuple vs class

1. nametuple 更省空间(没有class内置函数)
2. 使用tuple 可以直接对nametuple 进行初始化
'''

from collections import namedtuple



# example 1 , 手动初始化
# 参数1, type name, namedtuple 的 name
# 参数2, tuple内部的数据名称
User = namedtuple('User', ['name', 'age', 'gender'])
user = User(name='jiaxiang', age='24', gender='male')
print(user, user.name, user.age, user.gender)


# example 2, tuple 初始化(数据库添加场景)
User2 = namedtuple('User', ['name', 'age', 'gender'])
MySQL_info = ('wangqi', '26', 'male') # 数据库数据拆包直接送入namedtuple
user2 = User2(*MySQL_info)
print(user2)


## example 3, tuple 初始化(通过字典进行初始化)
User3 = namedtuple('User', ['name', 'age', 'gender', 'edu'])
info = {'name':'yutong', 'age':'25', 'gender':'male'}
user3 = User3(**info, edu='postgraduate')
print(user3)