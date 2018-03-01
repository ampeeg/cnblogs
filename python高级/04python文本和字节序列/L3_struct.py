# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午10:34
# @Author  : Clarence_Liao
# @FileName: L3_struct.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    struct可以从二进制序列中提取结构化信息。
    struct模块提供了一些函数，可以将打包的字节序列转换成不同类型字段组成的元组；还有一些函数用于执行反向转换。
    struct模块可以处理bytes、bytearray、memoryview对象。
'''

import struct

if __name__ == "__main__":
    # memoryview类用于共享内存，可以访问其他二进制序列、打包的数组和缓冲中的数据切片，该操作无需赋值字节序列
    fmt = '<3s3sHH'   # 设置格式，< 是小字节序，3s3s是两个3字节序列，HH是两个16位二进制整数

    with open('L3_图_python.jpg', 'rb') as f:
        img = memoryview(f.read())

    print(bytes(img[:10]))    # b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x02\x00\x1c\x00\x1c\x00\x00'
    print(struct.unpack(fmt, img[:10]))   # (b'\xff\xd8\xff', b'\xe0\x00\x10', 17994, 17993)  :拆包

    del img

