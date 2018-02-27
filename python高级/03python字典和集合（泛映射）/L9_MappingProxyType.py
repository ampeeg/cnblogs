# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午2:45
# @Author  : Clarence_Liao
# @FileName: L9_MappingProxyType.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/



'''
    python标准库里面的映射类型都是可变的，有时候需要使用不可变的映射，从python3.3开始，types模块中引入了
    MappingProxyType类，如果给这个类一个映射，那么它会返回这个映射的试图，该试图是动态的，原映射如果有改动
    可立即通过这个试图观察到，但是这个试图无法对该映射进行修改。
'''
from types import MappingProxyType

if __name__ == "__main__":
    d = {'one':1, 'two':2, 'three':3}
    d_proxy = MappingProxyType(d)
    print(d_proxy)     # {'three': 3, 'two': 2, 'one': 1}
    print(d_proxy['one'])  # 1
    for k, v in d_proxy.items():
        print(k, v)

    #d_proxy['four'] = 4   # 报错：TypeError: 'mappingproxy' object does not support item assignment
    d['four'] = 4
    print(d_proxy)     # {'two': 2, 'three': 3, 'four': 4, 'one': 1}