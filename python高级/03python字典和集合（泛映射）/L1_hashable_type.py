# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 下午8:56
# @Author  : Clarence_Liao
# @FileName: L1_hashable_type.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    可散列数据类型（也称可hash）————我理解"可散列"就是"可hash"
    可hash的对象需要实现__hash__方法，返回hash值；另外为了与其他对象比较还需要有__eq__方法

    原子不可变数据类型（str、bytes和数值类型）都是可散列的，可散列对象必须满足下列要求：
    （1）实现了__hash__方法，并且所得到的hash值是不变的
    （2）实现了__eq__方法，用来比较
    （3）若a == b 为真，那么hash(a) == hash(b)也是真
'''


# 创建类Foo，并实现__hash__和__eq__

class Foo:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        print("正在hash...")
        return hash(self.name)

    def __eq__(self, other):
        print("正在比较...")
        return self.name == other.name

    def __repr__(self):
        return self.name


if __name__ == "__main__":

    f1 = Foo("小李")
    f2 = Foo("小红")
    f3 = Foo("小李")

    s = set([f1, f2, f3])        # 集合实现不重复的原理正好利用了散列表
    print(s)                     # {小红, 小李}
    print( f1 == f3, hash(f1) == hash(f3))      # True True 满足可散列对象的第三个条件


'''
    对于元组来说，只有当一个元组包含的所有元素都是可hash的情况下，它才是可hash的
'''
t1 = (1, 2, 3, [1, 2])   # 元组里的列表的值是可变的，所以不可hash
try:
    print(hash(t1))
except Exception as e:
    print(e)             # unhashable type: 'list'

t2 = (1, 2, 3, (1, 2))   # 元组里的元素都是不可变的，并且第二层元组里面的元素也不可变，所以可hash
print(hash(t2))          # 3896079550788208169

t3 = (1, 2, 3, frozenset([1, 2]))
print(hash(t3))          # -5691000848003037416

