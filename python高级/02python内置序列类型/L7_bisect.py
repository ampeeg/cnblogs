# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 上午11:17
# @Author  : Clarence_Liao
# @FileName: L7_bisect.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

'''
    bisect模块主要用来管理有顺序的序列
    bisect模块包含的主要函数是bisect和insort，两个函数都使用二叉树方法搜索
    1、bisect(haystack, needle)
        haystack必须是一个有序的序列，该函数搜索needle在haystack中的位置，该位置使得将needle插入后haystack仍然升序
        查找到位置后可用haystack.insert（）插入

    2、insort(seq, item)
        把item插入到seq中，并能保持seq的升序

'''

#  本人认为《流畅的python》中的对该模块介绍的例子比较经典，故引用之

# 1、关于bisect.bisect的示例
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    '''   输出如下
    DEMO: bisect
    haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30
    31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31
    30 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |30
    29 @ 13      |  |  |  |  |  |  |  |  |  |  |  |  |29
    23 @ 11      |  |  |  |  |  |  |  |  |  |  |23
    22 @  9      |  |  |  |  |  |  |  |  |22
    10 @  5      |  |  |  |  |10
     8 @  5      |  |  |  |  |8 
     5 @  3      |  |  |5 
     2 @  1      |2 
     1 @  1      |1 
     0 @  0    0 
    '''
# 另，bisect.bisect函数有两个可选参数——lo和hi来缩小搜索范围，lo的默认值是0，hi的默认值是序列的长度
# 再另，bisect.bisect函数其实是bisect_right函数的别名，还有一个bisect_left，插入位置如果有相等的元素时，插入元素会放在它相等的
#      元素后面，后者会放在前面


# 根据分数，查到等级

def grade(score, breakpoints=[60, 70, 80, 90], grades = 'FDCBA'):
    i = bisect.bisect(breakpoints, score)     # 这里的bisect.bisect实际上使用的是bisect_right
    return grades[i]

print([grade(score) for score in [33, 55, 90, 87, 65, 78, 34, 60, 100]])



# 2、关于bisect.insort函数

import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

    '''输出：
    10 -> [10]
     0 -> [0, 10]
     6 -> [0, 6, 10]
     8 -> [0, 6, 8, 10]
     7 -> [0, 6, 7, 8, 10]
     2 -> [0, 2, 6, 7, 8, 10]
    10 -> [0, 2, 6, 7, 8, 10, 10]
    '''

# 另，insort函数也有insort_left