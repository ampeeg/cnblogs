# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 上午12:02
# @Author  : Clarence_Liao
# @FileName: L3_dict_1.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    字典是python内置类型中唯一的映射，先看创建字典的几种方法

    1、对象创建
    2、大括号
    3、zip
'''

if __name__ == "__main__":
    # 1、利用实例化对象的方法创建
    a = dict(key1=1, key2=2, all=[1, 2, 3])
    b = dict([('key3', 3), ('key4', 4)])
    c = dict({"key5": 5, "key6": 6})

    print("a:", a)     # a: {'key1': 1, 'all': [1, 2, 3], 'key2': 2}
    print("b:", b)     # b: {'key3': 3, 'key4': 4}
    print("c:", c)     # c: {'key6': 6, 'key5': 5}

    # 2、直接使用大括号
    d = {"key7": 7, "key8": 8}
    print("d:", d)     # d: {'key8': 8, 'key7': 7}

    # 3、使用zip
    e = dict(zip(("key9", "key10", "key11"), [9, 10, 11]))
    print("e:", e)     # e: {'key11': 11, 'key10': 10, 'key9': 9}