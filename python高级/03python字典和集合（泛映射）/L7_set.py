# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午2:12
# @Author  : Clarence_Liao
# @FileName: L7_set.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    集合对于很多人并不陌生，中学阶段就已经接触过。集合具有：
    （1）确定性：每一个对象都能确定是不是某一集合的元素，没有确定性就不能成为集合
    （2）互异性：集合中任意两个元素都是不同的对象
    （3）无序性：{a,b,c}{c,b,a}是同一个集合

    在python中，set中的元素必须是可散列的，但set本身不可散列(但是frosenset是可散列的)


    另外：set实现了很多基础运算
    &（交集）、|（并集）、-（差集）
'''


if __name__ == "__main__":
    # 创建集合
    s1 = set([1, 2, 3])
    s2 = {1, 2, 3, 4}
    print(s1, s2)     # {1, 2, 3} {1, 2, 3, 4}

    # 集合推导式
    s3 = {x**2 for x in range(10)}
    print(s3)         # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
