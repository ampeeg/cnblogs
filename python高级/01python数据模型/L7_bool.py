# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午2:42
# @Author  : Clarence_Liao
# @FileName: L7_bool.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

# 继续在上面列子中添加__bool__

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == "__main__":
    v = Vector(0, 3)
    if v:                     # 调用__bool__
        print(abs(v))        # 3.0

# 使用if或while语句，或者and\or\not运算符，为了判定一个对象v是真还是假，python会调用bool(v),这个函数只能返回True或者False
# 默认情况下，自定义的类的实例总被认为是真的，除非这个类对__bool__或者__len__函数有自己的实现。
# bool(v)后面是调用v.__bool__()的结果；如果不存在__bool__方法，那么bool(v)会尝试调用v.__len__()，若返回0，则bool返回False，否则为True

# python 3.6的官方文档如下介绍
'''
By default, an object is considered true unless its class defines either a __bool__() method that 
returns False or a __len__() method that returns zero, when called with the object. 
Here are most of the built-in objects considered false:

    constants defined to be false: None and False.
    zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
    empty sequences and collections: '', (), [], {}, set(), range(0)
Operations and built-in functions that have a Boolean result always return 0 or False for false 
and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and 
always return one of their operands.)
'''