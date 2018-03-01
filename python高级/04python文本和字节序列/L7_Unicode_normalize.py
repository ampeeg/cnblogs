# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 上午9:19
# @Author  : Clarence_Liao
# @FileName: L7_Unicode_normalize.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    初一看这个标题可能会有点蒙，难道Unicode本身还不够标准么？
    先看看以下的例子：
'''
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)     # café café
print(s1 == s2)   # False

'''
    我们发现café可以用'café'和'cafe\u0301'两种方式表示，这个词对于人来说是一样的，但是这两种表示对于计算机来说却是不一样的
    像这样的序列叫"标准等价物"，在计算机中存储的值不相等，但应用程序应该认为相等。
    
    要解决这个问题，需要用到unicodedata.nomalize函数，它的第一个参数可以选择这四种形式的一个："NFC"、"NFD"和"NFKC"、"NFKD"
        "NFC"：使用最少的码位构成等价的字符串
        "NFD"：把组合的字符分割成基本字符和单独的组合字符
        
        "NFKC"&"NFKD"：这两种是较严格的规范形式，对"兼容字符有影响"
'''

from unicodedata import normalize

if __name__ == "__main__":
    # "NFC" & "NFD"
    print(s1.encode('utf8'), s2.encode('utf8'))   # b'caf\xc3\xa9' b'cafe\xcc\x81'
    s1 = normalize("NFC", s1)
    s2 = normalize("NFC", s2)
    print(s1, s2)    # café café
    print(s1 == s2)  # True
    print(s1.encode('utf8'), s2.encode('utf8'))   # b'caf\xc3\xa9' b'caf\xc3\xa9'

    # "NFKC"&"NFKD"
    # 这两种方式会损失信息，所以不建议使用，除非一些特殊情况，比如搜索和索引中
    s3 = '½'
    print(normalize('NFKC', s3))    # 1⁄2    将½转换成了1⁄2
    s4 = '™'
    print(normalize('NFKC', s4))    # TM     将™转换成了TM


    '''
    另外，如果比较的时候不区分大小写，建议使用str.casefold(), 它与lower基本一致，其中大约有116个特殊的字符结果不同
    '''
    s5 = 'AKJkakshfKHDSdshfKSDShKkHkjhKJkgJhgJHkkHkjhJKhKJhK'
    print(s5.casefold())    # akjkakshfkhdsdshfksdshkkhkjhkjkgjhgjhkkhkjhjkhkjhk

