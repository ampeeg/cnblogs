# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午5:37
# @Author  : Clarence_Liao
# @FileName: L1_Sequence.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''

 所谓序列，即元素有序排列，python标准库用C实现了丰富的序列类型，按照序列中是否可存放不同类型的数据分为"容器序列"和"扁平序列"
 容器序列可以存放统统类型的数据，而扁平序列只能存放一种类型

    容器序列：list、tuple、collections.deque
    扁平序列：str、bytes、bytearray、memoryview、array.array

 按照是否能修改的标准序列又可分为"可变序列"和"不可变序列"：

    可变序列：list、bytearrary、array.arrary、collections.deque和memoryview
    不可变序列：tuple、str和bytes

 由于可变序列继承自不可变序列，所以可变序列继承的方法也较多，下面看看它们包含的方法：

                方法名              不可变序列            可变序列
             __contains__             有                   有
             __iter__                 有                   有
             __len__                  有                   有
             __getitem__              有                   有
             __reversed__             有                   有
             index                    有                   有
             count                    有                   有
             __setitem__                                   有
             __delitem__                                   有
             insert                                        有
             append                                        有
             reverse                                       有
             extend                                        有
             pop                                           有
             remove                                        有
             __iadd__                                      有

'''


