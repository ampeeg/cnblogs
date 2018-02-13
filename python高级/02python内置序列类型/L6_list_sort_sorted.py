# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 上午10:04
# @Author  : Clarence_Liao
# @FileName: L6_list_sort_sorted.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/



'''
    list.sort方法和sorted内置函数都有排序的功能，区别如下
        list.sort是就地排序列表，不会把原列表复制一份。该方法返回None，以提醒不会新建一个列表。
        sorted函数会新建一个列表作为返回值，这个函数可以接受任何可迭代对象，甚至包括不可变序列或生成器，最后返回的总是列表。

    list.sort和sorted都有两个参数：
        reverse：默认为False，设定为True以降序排列
        key：一个只有一个参数的函数，这个函数会作用于序列的每一个元素上，然后以该函数的结果作为关键字排序

'''

if __name__ == "__main__":
    # 1、list.sort就地排序，而sorted返回列表
    l = [x for x in range(10, 0, -1)]      # 初始化一个列表：[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(id(l), l)    # l最初的地址：4536449800 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    l.sort()
    print(id(l), l)    # 排序后的地址：4536449800 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                       # l前后的的地址没变，说明是就地排序


    l = [x for x in range(10, 0, -1)]  # 初始化一个列表：[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(id(l), l)  # l最初的地址：4415318984 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    l = sorted(l)
    print(id(l), l)  # 排序后的地址：4415318792 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 2、sorted可以接受任何可迭代对象
    l = (x for x in range(10, 0, -1))
    print(type(l))        # 迭代器 <class 'generator'>
    print(sorted(l))      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    s = "qwertyuiopasdfghjklzxcvbnm"   # 字符串序列
    print(sorted(s))      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    s = (1, 3, 2, 456, 345, 12, 2, 5, 78, 34)   # 不可变元组
    print(sorted(s))      # [1, 2, 2, 3, 5, 12, 34, 78, 345, 456]

    # 3、reverse参数
    s = "qwertyuiopasdfghjklzxcvbnm"
    print(sorted(s, reverse=True))   # ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


    # 4、key参数
    s = "QwERTYuioPaSdfGHjKLzXcvbnm"
    print(sorted(s))    # 大写在前 ['E', 'G', 'H', 'K', 'L', 'P', 'Q', 'R', 'S', 'T', 'X', 'Y', 'a', 'b', 'c', 'd', 'f', 'i', 'j', 'm', 'n', 'o', 'u', 'v', 'w', 'z']
    print(sorted(s, key=str.lower))   # 忽略大小写 ['a', 'b', 'c', 'd', 'E', 'f', 'G', 'H', 'i', 'j', 'K', 'L', 'm', 'n', 'o', 'P', 'Q', 'R', 'S', 'T', 'u', 'v', 'w', 'X', 'Y', 'z']
    print(sorted(s, key=str.upper))   # 也是忽略大小写



##########################
#
#  以下自定义一个类也可使用sorted函数
#
##########################

class Obj:
    def __init__(self):
        self.s = [x for x in range(10, 0, -1)]

    def __getitem__(self, item):
        print("getitem")
        return self.s[item]

    def __repr__(self):
        return str(self.s)

    def __iter__(self):
        return iter(self.s)

obj = Obj()
print(obj)           # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 添加getitem后可以使用sorted函数  （实验时请注释掉getitem方法）
print(sorted(obj))   #  打印10次getitem   ， [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 添加iter方法
print(sorted(obj))   # 此时解释器会先调用iter方法，不会再使用getitem方法
                     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]