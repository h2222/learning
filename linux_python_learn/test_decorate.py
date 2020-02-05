#! python
#coding=utf-8


'''
测试python 装饰器, 
装饰器的主要作用是简化重复代码, 提高代码复用性, 减少对原类或函数的修改

下面的例子为使用装饰器打印日志
'''


# 使用装饰器

# 装饰器的本质是接受接收一个函数(f),
# 装饰一下这个函数变成一个新函数(fn), 如果传输的函数需要传参, 可以在这一步直接传入
# 最后返回这个函数(fn)
def decorate(f):
    def fn(x):
        print('call', f.__name__)
        return f(x)
    return fn

# 再次强调, 函数, 也是对象, 所以内置函数
# 装饰器decorate的内置函数 包含了参数函数的名称打印和调用
# d1 = decorate(add_1)




# 如果不使用装饰器, 需要在每一个函数内打印信息
# 可以使用@使用装饰器, 效果就是函数
@decorate
def add_1(x):
    # print('call', add_1.__name__)
    return x+1

@decorate
def sub_1(x):
    # print('call', sub_1.__name__)
    return x-1



add_1(1)



# 带参数的 decorate
# 装饰器, 本质上就是函数的闭包
# 闭包函数的最外层函数返回的内置函数

def A(a):
    def B(b):
        def C(c):
            print ('a', a, 'b', b.__name__, 'c', c)
            return b(c)
        return B
    return A

# 可以看到 函数 A 返回 B , B 返回 C , C 打印信息
# 如果我们将A的参数作为装饰器的参数, B的参数作为要装饰函数
# 的参数(该参数是一个函数), C的参数作为被修饰函数的参数

r = A('装饰器参数')(add_1)(1)

# 带参数的 decorate
# 装饰器, 本质上就是函数的闭包
# 闭包函数的最外层函数返回的内置函数

# log 返回 log_decorator 函数的对象, log_decorator 返回wrapper函数的对象, 

def log(prefix):
    def log_decorator(f):
        def wrapper():
            print ('[%s] %s()...' % (prefix, f.__name__))
            return f()
        return wrapper
    return log_decorator


@log('DEBUG')
def test():
    pass
print (test())


my_func = log('DEBUG')(test)()
