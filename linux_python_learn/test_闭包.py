#! python
#coding=utf-8


'''
内层函数引用了外层函数的变量（参数也算变量），
然后返回内层函数的情况，称为闭包（Closure）

'''

def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print (f1(), f2(), f3())


'''
闭包的特点是返回的函数还引用了外层函数的局部变量，
所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变
'''
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
# 但返回的结果为9, 9, 9 , 为什么?
# 因为 for函数属于主函数, 且主函数count返回的为内置函数f()对象, 是整个
# 主函数流程的最后一步, 如果等for循环结束, i 早都等于3了
# 所以 在执行内置函数f()时, i一定为3, i*i就为9了

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

# 修改建议为 在主函数中直接执行内置函数
# 这样当外层函数的局部变量变化时, 保证了当变量被内置函数引用时固定唯一 
def count_fix():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()

print(f1(), f2(), f3())























