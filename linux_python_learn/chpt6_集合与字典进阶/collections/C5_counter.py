# coding = utf-8

'''
Counter 的使用, 统计可迭代对象(包括字符串, 算法刷题神器)
'''

from collections import Counter

# 统计list

lc = Counter([1, 2, 3,312 ,423 ,52, 5,2,3,5,3,1,1,54,5,2,3,5,1])
print(lc)

# 统计 string
sc = Counter('dasdadadafagsgsdsdfadSDASF')
print(sc)

# 更新
lc.update([1,2,3 , 4, 5, 6,46])
print('upadated lc:', lc)


# 更新2
sc.update(Counter('dasdasdasdasda'))
print('updated sc:', sc)



# top n 字符
mc_lc = lc.most_common(3)

print(mc_lc)
