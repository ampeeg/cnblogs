# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 下午5:53
# @Author  : Clarence_Liao
# @FileName: L8_Unicode_sort.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/



'''
    python比较序列时，会一一比较其中的元素。对于字符来说，比较的是其码位，主要是比较的ascii码；
    非ascii文本的标准排序方式是使用locale.strxfrm函数，但是使用这个函数必须事先设定区域，但有些操作系统不支持，并且改变区域设置并不十分合适

    建议使用pyuca.Collator.sort_key方法进行排序
'''



if __name__ == "__main__":
    # python默认的排序
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    print(sorted(fruits))    # ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']

                            # 但正确排序应该是：['açaí'，'acerola', 'atemoia', 'cajá', 'caju']

    # 使用pyuca.Collator.sort_key

    import pyuca
    print(sorted(fruits, key = pyuca.Collator().sort_key))   # ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

    # pyuca可以将自定义排序表路径传递给Collator()构造方法，pyuca默认使用自带的allkeys.txt