# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午7:15
# @Author  : Clarence_Liao
# @FileName: L4_tuple_unpacking.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/




# 我们经常这样给两个变量同时赋值
a, b = 1, 2
print(a, b)     # 1 2

# 还可以这样
a, b = [1, 2]
print(a, b)     # 1 2

# 也可以这样
a, b = (1, 2)
print(a, b)     # 1 2

# 甚至可以这样
a, b = "ab"
print(a, b)     # a b

'''
    像以上这样连续的赋值方式，右边可以使用逗号隔开；也可以是序列。
    
    当拆包赋值的是序列时，python解释器会先找该序列中的__iter__方法，如果该方法不存在，则寻找__getitem__方法。
       
    接下来说其他用法
'''

# 赋值后优雅地交换两个变量
a, b = (1, 2)
a, b = b, a
print(a, b)        # 2 1

# 使用*号来处理多余的数据
a, b, *s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, b, s)        # 1 2 [3, 4, 5, 6, 7, 8, 9]
                      # 这样从第三个元素开始的所有值都赋给了s

a, b, *s = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a, b, s)        # 1 2 [3, 4, 5, 6, 7, 8, 9]
                      # 注意，本来是元组，赋之后的s变成了列表. 如果s为空的话也会返回空列表

*s, a, b = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(s, a, b)        # [1, 2, 3, 4, 5, 6, 7] 8 9
                      # *s也可以放在前面

a, *s, b = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a, s, b)        # 1 [2, 3, 4, 5, 6, 7, 8] 9
                      # *s也可以放在中间

# 嵌套元组拆包
a, b, (c, d) = (1, 2, (3, 4))
print(a, b, c, d)     # 1 2 3 4
                      # 只要按照右边的形式就可赋值

a, b, *c = (1, 2, (3, 4))
print(a, b, c)     # 1 2 [(3, 4)]







################################
#
# 以下的例子用以说明拆包赋值时，解释器会按照__iter__、__getitem__的顺序调用类中的方法
#
################################
class Foo:
    def __init__(self, s):
        self.s = s

    def __iter__(self):
        print("iter")
        return iter(self.s)

    def __getitem__(self, item):
        return self.s[item]

if __name__ == "__main__":
    foo = Foo("sdfafasfasf")
    a, b, *s = foo
    print(a, b)




#######################
#
# 测试元组是否存在就地拼接
#
#######################
a = (2,3,4)
b = (3,4,5)
print(id(a))
a +=b
print(a, id(a))