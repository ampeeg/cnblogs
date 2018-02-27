# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 下午11:29
# @Author  : Clarence_Liao
# @FileName: L5_dict_3.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/



'''
    处理找不到的键

    在实际场景中，当使用d[key]的方法查找数据的时候，如果找不到该键，python会抛出KeyError异常；
    如果是取值操作，可以使用d.get(key, default)来解决，可以给找不到的键一个默认的值
    但是如果要给更新某个不存在键对应的值的时候，就稍显麻烦了，可以使用以下方法解决：
        1、用setdefault处理dict找不到的键
        2、使用defaultdict对象
        3、__missing__方法
'''

class Foo:
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return str(self.name)

    def setattr(self, key, value):
        self.__setattr__(key, value)
        return self


if __name__ == "__main__":
    d1 = {}
    print(d1.get("key", "default"))   # default   使用d.get(key, default)的方法取值


    # 1、用setdefault处理dict找不到的键
    d2 = {}
    d2.setdefault("key", [x for x in "adfaf"])  # setdefault虽然是set名字，但是是取值操作，只有当键不存在时才进行赋值，并返回该值
    l = d2.setdefault("key", [])
    print(l)                                    # ['a', 'd', 'f', 'a', 'f']

    d2.setdefault("key2", []).extend([1, 2, 3]) # 返回空列表，所以可在后面直接使用方法extend
    print(d2)                                   # {'key': 'default', 'key2': [1, 2, 3]}

    # 2、使用defaultdict对象
    #  在python中，还有一些dict的变种类型，defaultdict为其中一种，位于collections中
    from collections import defaultdict

    dic = defaultdict(list)                    # 将list的构造方法作为default_factory（只有__getitem__找不到值时调用）
    dic["key"].extend([1, 2, 3])               # dic中不含有"key"键，此时default_factory会被调用，创造一个空列表,并连接[1, 2, 3]
    print(dic["key"])                # [1, 2, 3]

    dic = defaultdict(Foo)           # 将Foo的构造方法作为default_factory创建一个defaultdict
    print(dic["key"].setattr("name", "default"))                # default

    # 3、__missing__方法
    # 所有的映射类型在找不到键的时候，都会牵扯到__missing__方法；如果在__getitem__找不到键的时候，python就会自动调用它
    # 另外，__missing__方法只会被getitem调用，对get或者__contains__没有影响

    class My_dict(dict):
        def __missing__(self, key):
            print("正在调用__missing__...")

    mdict = My_dict(one=1, two=2, three=3)
    print(mdict)     # {'two': 2, 'three': 3, 'one': 1}
    mdict["key"]     # 正在调用__missing__...

