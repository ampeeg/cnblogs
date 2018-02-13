# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午6:29
# @Author  : Clarence_Liao
# @FileName: L2_list_comprehension.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


# 列表推导式生成的是列表，会占用系统内存
# 基本语法

list_1 = [x for x in range(1, 20)]
list_2 = [x ** 2 for x in range(1, 20)]


print(list_1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list_2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

# 笛卡尔积型的列表推导式
list_3 = [(x, y) for x in range(1, 3)        # 1，2
                 for y in range(7, 10)]      # 7、8、9

                                             # 该表达式会先将1分别和7、8、9组合，然后再拿2和7、8、9组合，共6对
print(list_3)  # [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9)]


list_4 = [x+y for x in range(1, 3)
                 for y in range(7, 10)]

print(list_4)   # [8, 9, 10, 9, 10, 11]

# 还可以添加if语句
l = [1, 3, 4, 33, 45, 36, 422, 34, 67, 23, -4, -7, -345, 46, -6, -45, 32, -8, -4, 67, -4]

list_5 = [x for x in l if x > 0]   # 只取出大于0的生成列表
print(list_5)                      # [1, 3, 4, 33, 45, 36, 422, 34, 67, 23, 46, 32, 67]
