import bisect


'''
掌握理解bisect
使用bisect向列表添元素时, 实现自动排序
bisect 为二分查找, 性能很高
'''

temp_list = []

bisect.insort(temp_list, 4)
bisect.insort(temp_list, 3)
bisect.insort(temp_list, 6)
bisect.insort(temp_list, 1)
bisect.insort(temp_list, 0)
bisect.insort(temp_list, 9)

# 查询, 返回9的index 
print(bisect.bisect(temp_list, 9))

# 测试
print('测试bisect排序功能:', temp_list)



