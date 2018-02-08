# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 上午12:36
# @Author  : Clarence_Liao
# @FileName: L4_for_i_in_x.py
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

    def __iter__(self):
        return iter(self._stock)

    # def __contains__(self, item):
    #     print(item)
    #     return False

if __name__ == "__main__":
    foo = Foo()
    for i in foo:        # 重写了__iter__(self)后解释器自动执行iter（foo）
        print(i)

    x = iter(foo)       # 手动执行
    print(next(x))      # stock(name=1, price=1)
    print(next(x))      # stock(name=2, price=2)
    print(next(x))      # stock(name=3, price=3)

    print(Stock(name=4, price=4) in foo)    #  按照__contains__、__iter__、__getitem__顺序寻找：True
