 # -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午11:03
# @Author  : Clarence_Liao
# @FileName: L4_encode_decode.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    python自带有超过100中编解码器，用于在字符串和字节之间相互转换。
    每个编码都有多个名称，例如'utf_8'、'utf8'、'utf-8'、'U8'，这些都可以传递给open()、str.encode()、bytes.decode()中的
    encoding参数
'''


if __name__ == "__main__":
    # 看看不同的编码效果
    for codec in ['gbk', 'utf8', 'utf16']:
        print(codec, "你好".encode(codec), sep='\t')
    '''
                        gbk	  b'\xc4\xe3\xba\xc3'
                        utf8	b'\xe4\xbd\xa0\xe5\xa5\xbd'
                        utf16	b'\xff\xfe`O}Y'
    '''
    # 咱们再来解码
    print(b'\xc4\xe3\xba\xc3'.decode('gbk'))            # 你好
    print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))   # 你好
    print(b'\xff\xfe`O}Y'.decode('utf16'))              # 你好