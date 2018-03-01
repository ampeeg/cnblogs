# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午11:39
# @Author  : Clarence_Liao
# @FileName: L5_UnicodeError.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

'''
    遇到编码问题一般很烦躁，下面来看看一般怎么解决编码问题。
    （1）UnicodeEncodeError
     (2) UnicodeDecodeError
'''



if __name__ == "__main__":
    # (1）UnicodeEncodeError
    # 使用errors参数
    s1 = "hello，你长胖啦".encode('latin-1', errors='ignore')
    print(s1)   # b'hello'    使用 errors='ignore' 忽略了无法编码的字符

    s2 = "hello，你长胖啦".encode('latin-1', errors='replace')
    print(s2)   # b'hello?????'    使用errors='replace'将无法编码的字符用问好代替

    s3 = "hello，你长胖啦".encode('latin-1', errors='xmlcharrefreplace')
    print(s3)   # b'hello&#65292;&#20320;&#38271;&#32982;&#21862;'  使用errors='xmlcharrefreplace'将无法编码的内容替换成XML实体

    # (2) UnicodeDecodeError
    # 乱码字符称为鬼符，以下实例演示出现鬼符的情况

    s4 = b'Montr\xe9al'
    print(s4.decode('cp1252'))    # Montréal
    print(s4.decode('iso8859_7')) # Montrιal
    print(s4.decode('koi8_r'))    # MontrИal
    #print(s4.decode('utf8'))      # 报错：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
    print(s4.decode('utf8', errors='replace'))   # Montr�al


    '''
        大多数人都遇到过乱码问题，并且可能总是调试不成功，这可能是各种程序之间的编码不匹配
        以下代码引用自<流畅的python>，可以用来查看当前环境的一些默认编码     
    '''

    # -*- coding: utf-8 -*-

    import sys, locale

    expressions = """
            locale.getpreferredencoding()
            type(my_file)
            my_file.encoding
            sys.stdout.isatty()
            sys.stdout.encoding
            sys.stdin.isatty()
            sys.stdin.encoding
            sys.stderr.isatty()
            sys.stderr.encoding
            sys.getdefaultencoding()
            sys.getfilesystemencoding()
        """

    my_file = open('dummy', 'w')

    for expression in expressions.split():
        value = eval(expression)
        print(expression.rjust(30), '->', repr(value))

    '''
        我电脑运行结果如下：
        (' locale.getpreferredencoding()', '->', "'UTF-8'")
        ('                 type(my_file)', '->', "<type 'file'>")
        ('              my_file.encoding', '->', 'None')
        ('           sys.stdout.isatty()', '->', 'True')
        ('           sys.stdout.encoding', '->', "'UTF-8'")
        ('            sys.stdin.isatty()', '->', 'True')
        ('            sys.stdin.encoding', '->', "'UTF-8'")
        ('           sys.stderr.isatty()', '->', 'True')
        ('           sys.stderr.encoding', '->', "'UTF-8'")
        ('      sys.getdefaultencoding()', '->', "'ascii'")
        ('   sys.getfilesystemencoding()', '->', "'utf-8'")
    '''