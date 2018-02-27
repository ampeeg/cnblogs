# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 下午11:26
# @Author  : Clarence_Liao
# @FileName: L2_mapping.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    泛映射类型就是广义上的对应关系，在数学中，我们将集合A对应集合B中的对应法则称为"映射"（Mapping）
    同样，在python里，我们称"键值对"为映射，这其实也是一种对应法则
    如果一个数据类型是映射，那么它肯定属于collections.abc.Mapping，可使用isinstance函数测试

    PS: 字典是 Python 语言中唯一的映射类型。映射类型对象里哈希值(键) 和指向的对象(值)是一对多的关系。
'''

from collections import abc
'''大家可以查看_collections_abc.py源代码，里面基本的类型包含:
    ["Awaitable", "Coroutine", "AsyncIterable", "AsyncIterator",
    "Hashable", "Iterable", "Iterator", "Generator",
    "Sized", "Container", "Callable",
     "Set", "MutableSet",
     "Mapping", "MutableMapping",
     "MappingView", "KeysView", "ItemsView", "ValuesView",
     "Sequence", "MutableSequence",
    "ByteString",
    ]
'''

# 我们测试一些常用的类型是不是映射
if __name__ == "__main__":
    print(isinstance({}, abc.Mapping))      # True   字典是典型的键值对
    print(isinstance([1, 2], abc.Mapping))  # False  列表是序列
    print(isinstance((1, 2), abc.Mapping))  # False  元组是序列
    print(isinstance('adfasfd', abc.Mapping))  # False  字符串也是序列
    print(isinstance(set(), abc.Mapping))  # False  集合不是映射
    print(isinstance(set(), abc.Sequence))  # False  集合也不是序列，没有先后顺序




'''
    如果我们自己想定义一个映射类型的对象，那么必须实现__getitem__、__iter__、__len__方法
    
    PS：关于该部分的原理，本人暂未查看说明文档，毕竟现实中几乎不可能自定义映射；有兴趣的同志可深入钻研。
'''


class Foo(abc.Mapping):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        return self.name

    def __iter__(self):
        return iter(str(self.name))

    def __len__(self):
        return len(self.name)


print(isinstance(Foo("123"), abc.Mapping))      # True
