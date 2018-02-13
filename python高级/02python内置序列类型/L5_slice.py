# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 上午9:17
# @Author  : Clarence_Liao
# @FileName: L5_slice.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    在python中，内置的序列类型都支持切片操作，切片操作的用法十分简单：
    list[start: stop: step]    , 其中不包括区间范围内最后一个（事实上这是python的风格，一般不包含区间最后一个）
    python里面能使用切片操作是因为实现了__getitem__方法，切片时会给该方法传递slice(start: stop: step) 参数
'''

if __name__ == "__main__":
    # 基本操作
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(l[2:])     # 第3个元素到最后   ：[3, 4, 5, 6, 7, 8, 9]
    print(l[:3])     # 第一个元素到最后   ：[1, 2, 3]

    s = "abcdefghijklmn"
    print(s[2::2])   # 从第三个字母开始，隔一个字母取一个 : cegikm
    print(s[::-1])   # 倒序排列 ： nmlkjihgfedcba
    print(s[::-2])   # 倒序隔一个取一个 nljhfdb
    print(s[-2::-2]) # 倒序第二隔开始，隔一个取一个

    # 利用切片赋值
    l[2:5] = [20, 30]
    print(l)         # [1, 2, 20, 30, 6, 7, 8, 9]
    try:
        l[2:5] = 40      # 报错：TypeError: can only assign an iterable
                         # 利用切片赋值时传入的必须是可迭代对象
    except Exception as e:
        print(e)         # can only assign an iterable
    l[2:5] = (40,)
    print(l)             # [1, 2, 40, 7, 8, 9]
    l[2:3] = "sajfljls"  # 字符串属于序列，也可以迭代
    print(l)             # [1, 2, 's', 'a', 'j', 'f', 'l', 'j', 'l', 's', 7, 8, 9]