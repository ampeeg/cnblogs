# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午1:10
# @Author  : Clarence_Liao
# @FileName: L5_repr.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


# 接下来的例子引用自《流畅的python》
# 创建一个二维向量的类Vector，慢慢给它添加一些运算

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'repr: Vector(%r, %r)' % (self.x, self.y)

    # def __str__(self):        # 如果类中同时有__str__和__repr__，则调用print时会先使用__str__
    #     return "str: Vector(%r, %r)" % (self.x, self.y)

# 这个类中现在只实现了__repr__方法

if __name__ == "__main__":
    v = Vector(2, 3)
    print(v)          # 此时打印出来的不是<Vector object at 0x0000003>这种形式
                      # 打印出来的是Vector(2, 3)
                      # 如果类中实现了__str__同样有此作用

# __repr__和__str__的区别在于，后者是在str()函数中被使用，或是在用print打印函数打印一个对象的时候才被
# 调用。如果你只想实现这两个特殊方法中的一个，__repr__是更好的选择，因为如果一个对象没有__str__函数
# 而python又需要调用它的时候，解释器会用__repr__作为代替

# 故使用print()函数时，解释器会按照__str__、__repr__的顺序寻找