#! python 
# coding = utf-8



'''
推导式性能高于for循环
'''



list_1 = []
for i in range(10):
    if i%2 == 0:
        list_1.append(i)


# 列表推导式(顺序安装嵌套顺序)
list_1 = [i for i in range(10) if i%2 == 0]



# 字典推导式
dict_1 = {1:'s', 2:'a', 3:'d'}
dict_2 = {value:key for key, value in dict_1.items()}



# 生成器表达式(小括号)
gen_1 = (i for i in range(10))
print(next(gen_1), next(gen_1), next(gen_1))






