# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 上午8:54
# @Author  : Clarence_Liao
# @FileName: L2_h_function.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    我们一般将函数分为"普通函数"和"高阶函数"，接受函数为参数的函数为高阶函数，其余为普通函数

    普通函数大家再熟悉不过，本文不讲，主要讲一下map、filter、reduce三个高阶函数
'''


if __name__ == "__main__":
    # map第一个参数接受一个函数，并将这个函数作用于后面可迭代对象的每一个元素中
    l = map(lambda x : x ** 2, range(11))   # 返回的是生成器类型
    print(list(l))     # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    w = map(str.upper, 'asfafasfasfaf')
    print(list(w))     # ['A', 'S', 'F', 'A', 'F', 'A', 'S', 'F', 'A', 'S', 'F', 'A', 'F']

    # filter第一个参数也接受函数，并返回所有满足该函数的元素
    l = filter(lambda n: n % 2, range(10))   # 返回n % 2为真的数,就是奇数
    l2 = filter(lambda n: n % 2 ==0, range(10))  # 返回偶数
    print(list(l))                           # [1, 3, 5, 7, 9]
    print(list(l2))                          # [0, 2, 4, 6, 8]

    # reduce 从python3开始，reduce放在functools中
    # reduce将某个操作连续应用到序列元素上，即其会将前一步的结果继续应用到下一个元素上
    from functools import reduce
    s = reduce(lambda x,y: x + y, range(101))
    print(s)       # 5050 对1到100求和
