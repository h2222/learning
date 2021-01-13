


'''
If you need to invoke a special method, it is usually better to call the related built-in function (e.g., len, iter, str, etc). 
for built-in types are faster than method calls.
'''


# implemented a 2-d vector that can be added, multiplied, if it is None, and re-print

from math import hypot

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # can print
    #If you only implement one of these special methods, choose __repr__, 
    # because when no custom __str__ is available, Python will call __repr__ as a fallback.
    def __repr__(self):
        return 'Vector( %r, %r)' % (self.x, self.y)
    # can abs()
    def __abs__(self):
        return hypot(self.x, self.y)
    # can if 
    def __bool__(self):
        return bool(abs(self))
    # can +
    def __add__(self, other_vector):
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector(x, y)
    # can *
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v = Vector(3, 4)
v2 = Vector(3, 4)
print(v)
v3 = v + v2
print(v3)
v4 = v * 3
print(v4)




