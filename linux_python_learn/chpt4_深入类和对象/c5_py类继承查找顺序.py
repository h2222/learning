#! python
# coding=utf-8


'''
类继承查找顺序


环状继承
      D1
    /   \
   B1    C1
    \    /
      A1

树状继承
   D2   E2
   |    |
   B2   C2
   \    /
     A2

'''
# 环状继承顺序(BFS)
class D1:
    pass
class B1(D1):
    pass
class C1(D1):
    pass
class A1(B1, C1):
    pass

print(A1.__mro__)


# 树状继承顺序(DFS)
class D2:
    pass
class E2:
    pass
class B2(D2):
    pass
class C2(E2):
    pass
class A2(B2, C2):
    pass

print(A2.__mro__)




