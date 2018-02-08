# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 下午11:55
# @Author  : Clarence_Liao
# @FileName: L3_getitem.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

from collections import namedtuple

Stock = namedtuple("stock", ["name", "price"])


class Foo:
    def __init__(self):
        self._stock = [Stock(name, price) for name, price
                                          in zip(range(1, 100), range(1, 100))]

    def __len__(self):
        return len(self._stock)

    def __getitem__(self, item):
        print(item)
        return self._stock[item]


if __name__ == "__main__":
    foo = Foo()
    print(len(foo))
    print(foo[3])    # 使用foo[3]时会调用__getitem__方法，解释器会将3传递给__getitem__(self, item)中的item参数
                     # stock(name=4, price=4)

    print(foo[3:6])  # 使用切片操作时也会调用__getitem__方法，解释器会传递slice(3, 6, None)item参数
                     # [stock(name=4, price=4), stock(name=5, price=5), stock(name=6, price=6)]


if __name__ == "__main__":
    # 此时可直接用for循环对foo进行遍历
    for i in foo:
        print(i)

    # 由于实现了__getitem__方法，foo实例就变成了可迭代对象
    # 不仅可以使用for循环正向迭代，也可反向迭代；还可以使用in判断
    for i in reversed(foo):
        print(i)     # 反向迭代

    print(Stock(name=2, price=2) in foo)  # in判断会先调用__contains__方法，但是如果没有该方法，则调用__getitem__按顺序迭代搜索
                                          # True  (调用了2次getitem)
    print(Stock(name=2, price=3) in foo)  # False (调用了100次getitem方法，最后一次foo[99]发现不存在而停止迭代)


