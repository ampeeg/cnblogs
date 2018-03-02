# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 下午2:11
# @Author  : Clarence_Liao
# @FileName: L5_annotation.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    函数注解很简单，用下面例子简单讲解即可明了
'''


if __name__ == "__main__":
    def foo(num: int, step: 'int 间隔(大于0小于num)'=1) -> int:
        ''':returns 求num的阶乘，可以设置步长'''     # 这里的注释存储在__doc__中
        return num if num <= step else num * foo(num-step,step)

    print(foo(5))  # 120   (5*4*3*2*1)
    print(foo(5, 2))  # 15 (5*3)

    # 函数声明中的各个参数可以在冒号（：）之后增加注释，该注释可以直接写参数类型，也可以写字符串
    # -> 符号后面是对函数返回值进行注解

    # 这些注释内容存储在属性 __annotations__中
    print(foo.__annotations__)  # {'step': 'int 间隔(大于0小于num)', 'num': <class 'int'>, 'return': <class 'int'>}

    # 这样注释后，在使用pycharm时会出现自动提示
