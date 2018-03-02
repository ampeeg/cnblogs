# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 上午8:34
# @Author  : Clarence_Liao
# @FileName: L1_f_object.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    在python中，"一等对象"指的是满足下述条件的程序实体：
    （1）在运行时创建
    （2）能赋值给变量或数据结构中的元素
    （3）能作为参数传给函数
    （4）能作为函数的返回结果

    整数、字符串和字典都是一等对象。在面向对象编程中，函数也是对象，并满足以上条件，所以函数也是一等对象，称为"一等函数"
'''


if __name__ == "__main__":
    # 函数的一等性质
    def foo(n):
        '''returns  n!'''
        return 1 if n < 2 else n * foo(n-1)

    print(foo(5))    # 120

    my_foo = foo
    print(my_foo)    # <function foo at 0x1010e3f28> 能赋值给变量
    print(list(map(my_foo, range(6))))   # [1, 1, 2, 6, 24, 120]   能赋值给函数

    def foo2():
        return foo

    my_foo2 = foo2()
    print(my_foo2(5))     # 120 可作为函数的返回结果