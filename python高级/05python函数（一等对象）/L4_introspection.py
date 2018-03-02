# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 上午9:52
# @Author  : Clarence_Liao
# @FileName: L4_introspection.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    函数内省我们通过例子来看
'''


if __name__ == "__main__":
    # 先创建一个函数
    def foo(n):
        ''':returns n!'''
        return 1 if n<2 else n*foo(n-1)

    print(foo.__doc__)   # :returns n!   __doc__里面存储了注释内容

    # 看看这个函数中有多少属性
    print(dir(foo))
    '''
        ['__annotations__', '__call__', '__class__', '__closure__', '__code__', 
        '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
        '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', 
        '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', 
        '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', 
        '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    '''

    # 下表对一些属性做了说明