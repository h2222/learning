# coding=utf-8



'''
deque double end queue 双端队列
1. appendleft  append (right)
2. deque 是线程安全的, list是线程不安全的
'''

from collections import deque

# 左右添加
dq = deque([1, 3, 5, 7])
dq.appendleft(2)
dq.append(10)
print(dq)

# 右侧扭转
dq.rotate()
print(dq)

# 左侧扭转
item0 = dq.popleft()
dq.append(item0)
print(dq)