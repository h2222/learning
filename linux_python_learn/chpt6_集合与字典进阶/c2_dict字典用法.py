#! python
# coding = utf-8


'''
字典常见用法
'''

a = {
     'hao':{'company':'bairong'},
     'wang':{'company':'tengxun'}
    }


# 深拷贝与浅拷贝
# 深拷贝 import copy   cp = copy.deepcopy(a)
# 浅拷贝
ac = a.copy()



# fromkeys 方法从list创建字典
# fromkeys 为dict的类对象函数, 不需要实例化dict对象
k = [1, 2, 3, 4]
v = 'default' # 每一个list对象的初始化
ak  = dict.fromkeys(k, v)
# 其他方式
ak = {k:'deafult' for k in k}
print(ak, '\n')


#set default 函数, 起始就是翻版的get(x, p)函数 判断x是否在字典的k中, 
# 如果在返回结果, 不在就是将k[x]等于p
a.setdefault('zhang',{'company', 'baidu'})
print(a)


# clear pop 等其他方法





