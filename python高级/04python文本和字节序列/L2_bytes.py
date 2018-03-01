# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午7:30
# @Author  : Clarence_Liao
# @FileName: L2_bytes.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    python3中内置有两种基本的二进制序列类型：不可变的bytes和可变bytearray
        （1）bytes和bytearray的各个元素是介于0～255（8个bit）之间的整数；
        （2）二进制序列的切片始终是同一类型的二进制序列
'''


if __name__ == "__main__":
    # 创建bytes 和 bytearray
    b1 = bytes('abc你好', encoding='utf8')      # 关于encode稍后会说，不知道有没有人和我一样总是将编码与解码的方向混淆
    print(b1)          # b'abc\xe4\xbd\xa0\xe5\xa5\xbd'

    b2 = bytearray('abc你好', encoding='utf8')
    print(b2)          # bytearray(b'abc\xe4\xbd\xa0\xe5\xa5\xbd')

    # 切片（提示：序列都可以切片）
    print(b1[3:5])     # b'\xe4\xbd'
    print(b2[3:5])     # bytearray(b'\xe4\xbd')

    # 使用列表取值的方法试试
    print(b1[3])       # 228 此时取出来的就不是字节序列了，而是一个元素
    for _ in b1:
        print(_, end=',')   # 97,98,99,228,189,160,229,165,189,      这都是8bit的整数

    # bytes的不可变 vs. bytearray的可变

    # b1[3] = 160           # 报错：'bytes' object does not support item assignment
    print(id(b2), b2)      # 4373768376 bytearray(b'abc\xe4\xbd\xa0\xe5\xa5\xbd')
    b2[2] = 78
    print(id(b2), b2)      # 4373768376 bytearray(b'abN\xe4\xbd\xa0\xe5\xa5\xbd')

    # 将b2转换成字符串看看
    print(b2.decode('utf8'))  # abN你好
                              # 注意，这里之所以能够用utf8转成unicode，是因为N的ascii码和utf8一致
    b2.extend(bytearray('添加的内容', encoding='utf8'))  # 既然是可变序列，bytearray当然拥有一般的序列的方法
    print(id(b2), b2)         # 4373768376 bytearray(b'abN\xe4\xbd\xa0\xe5\xa5\xbd\xe6\xb7\xbb\xe5\x8a\xa0\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9')

    print(b2.decode('utf8'))  # abN你好添加的内容

    # PS：大家可以将二进制序列当成列表，元素就是ascii编码（0～255）