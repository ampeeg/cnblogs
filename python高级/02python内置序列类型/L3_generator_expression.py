# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午6:49
# @Author  : Clarence_Liao
# @FileName: L3_generator_expression.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/



# 虽然列表推导式可以用来初始化元组、数组或其他序列类型，但是列表推导式会直接生成列表，占用内存
# 而生成器遵守了迭代器协议，可以逐个产出元素，而不是先建立一个完整的列表


# 生成器表达式直接将推导式的方括号换成圆括号即可

g = (x for x in range(1, 10000))

print(g)    # <generator object <genexpr> at 0x105c0efc0>：生成器对象


from collections import Iterable, Iterator

if isinstance(g, Iterable):
    print("iterable")          # 输出iterable: 说明生成器g是可迭代的

if isinstance(g, Iterator):
    print("iterator")          # 输出iterator：说明生成器g是迭代器



# 比较列表推导式和生成器
import time

start_time = time.time()
l = [x for x in range(1000000)]
print(time.time() - start_time)     # 0.1361069679260254

start_time = time.time()
g = (x for x in range(1000000))
print(time.time() - start_time)     # 1.1205673217773438e-05

# 可见，生成器远快于推导式
# 生成器只可用next()方法调用，不能用list[]取值
print(next(g))       # 0
print(next(g))       # 1
print(next(g))       # 2
print(next(g))       # 3

print(g[4])          # 报错：TypeError: 'generator' object is not subscriptable


# 生成器生成元组