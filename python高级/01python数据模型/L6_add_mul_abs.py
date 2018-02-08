# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午2:30
# @Author  : Clarence_Liao
# @FileName: L6_add_mul_abs.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

# 接上面的二维向量的例子

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):                         # abs本来是绝对值，在二维向量中指模
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)



if __name__ == "__main__":
    v = Vector(4, 3)
    # 使用abs()求模，解释器自动调用__abs__方法
    print(abs(v))       # 5.0

    # 使用+求向量加法，解释器自动调用__add__方法
    v2 = Vector(1, 5)
    print(v + v2)       # Vector(5, 8)
                        # ps: __add__方法返回的是Vector对象，然后print函数会调用__repr__
    # 使用*求向量与数的乘法，解释器自动调用__mul__方法
    print(v * 3)        # Vector(12, 9)
                        # 这里只实现了向量的数乘, 并且未实现 3*v
