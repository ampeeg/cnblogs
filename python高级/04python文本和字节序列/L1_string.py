# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午7:04
# @Author  : Clarence_Liao
# @FileName: L1_string.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    字符编码问题是经常困扰python编程人员的问题，我在编写爬虫的过程中也经常遇到这个头疼的事。

    从python3开始，明确区分了人类语言（文本字符串）和机器语言（二进制字节），咱们先说文本字符串
    开始之前，得对"字符"进行定义：
        字符：Unicode字符，从python3的str对象中获取的元素是Unicode字符
        字符串：字符串就是一个字符序列（这里对于（一）中内容相呼应）

'''


if __name__ == "__main__":
    # 创建字符
    s1 = str('a')
    s2 = 'b'
    s3 = u'c'
    print(s1, s2, s3)      # a b c
