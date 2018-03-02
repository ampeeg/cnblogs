# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 上午9:30
# @Author  : Clarence_Liao
# @FileName: L3_callable.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    我们在使用函数或者实例化对象的时候会用到括号（即()），这个括号实际上是调用运算符，python里面有7中可调用对象：

    1、用户定义的函数
        def和lambda创建
    2、内置函数
        使用C语言实现的函数，如len或time.strftime
    3、内置方法
        使用C语言实现的方法，如dict.get
    4、方法
        在类的定义体中定义的函数
    5、类
        调用类时其实首先运行的是__new__方法，然后运行__init__方法。这里很有意思，自定义类中其实没有重写__new__方法，
        而是调用的超类的__new__方法，如果查看源代码的实现逻辑，相信你会有新的发现，这里不做讨论。
    6、类的实例
        如果类定义了__call__方法，那么它的实例可以作为函数调用
    7、生长器函数
        使用yield关键字的函数或方法。
'''


if __name__ == "__main__":
    # 创建一个自定义可调用类
    class Foo():
        def __init__(self):
            self.name = "Foo"
        def __call__(self, *args, **kwargs):
            print("调用__call__")

    Foo()()     # 输出：调用__call__

    # 以上使用 Foo()() 这种写法看上去很有意思。首先，Foo()会创建一个Foo实例，调用__init__构造方法，; 然后使用实例(),此时
    # 调用__call__方法