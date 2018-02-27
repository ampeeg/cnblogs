# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午1:29
# @Author  : Clarence_Liao
# @FileName: L6_dict_4.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/



'''
    在python中虽然只有dict为映射类型，但是dict有很多变种，上面defaultdict就是，除此之外还有：

    （1）OrderedDict: 有顺序的字典
     (2) ChainMap： 可以容纳数个不同的映射对象
     (3) Counter：  给键准备一个整数计数器，每次更新键的时候会增加该计数器
    （4）UserDict：  将标准的dict用python实现了一遍
'''


from collections import OrderedDict, ChainMap, Counter, UserDict

if __name__ == "__main__":
    # 1、OrderedDict
    d = OrderedDict()
    d['one'] = 1
    d['two'] = 2
    d['three'] = 3
    for _ in range(10):
        print("%d次：" % _)
        for k, v in d.items():
            print("**", k, v)        # OrderedDict迭代的时候的顺序总是跟插入顺序一致


    # 2、ChainMap

    pylookup = ChainMap(d, globals())   # d和globals()都是映射类型，ChainMap会将其组合
    for v, k in pylookup.items():
        print(v, k)

    # 3、Counter
    ct = Counter('asfjlajslfjals')
    print(ct)      # Counter({'j': 3, 'l': 3, 's': 3, 'a': 3, 'f': 2})
                   # 存储的是每个字母出现的次数
    ct.update('jjjjjjjjlllllllll')
    print(ct)      # # Counter({'l': 12, 'j': 11, 's': 3, 'a': 3, 'f': 2})

    import random
    ct2 = Counter([random.randrange(1, 5) for _ in range(100)])   # 列表推导式创建Counter
    print(ct2)     # Counter({1: 30, 2: 24, 4: 24, 3: 22})

    ct3 = Counter((random.randrange(1, 5) for _ in range(100)))   # 生成器创建Counter
    print(ct3)      # Counter({2: 40, 3: 23, 4: 20, 1: 17})

    class Foo:
        def __init__(self, num):
            self.l = [random.randrange(1, 5) for _ in range(num)]

        def __iter__(self):
            return iter(self.l)

    ct4 = Counter(Foo(100))            # 可迭代对象创建Counter
    print(ct4)      # Counter({2: 31, 3: 25, 4: 25, 1: 19})

    # 4、UserDict
    # 创建自定义的映射类型，一般以UserDict为基类

    class My_dict(UserDict):
        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]

        def __contains__(self, key):
            return str(key) in self.data

        def __setitem__(self, key, item):
            print("调用__setitem__。。。")
            self.data[str(key)] = item

    mdict = My_dict()
    mdict["one"] = 1      # 调用__setitem__。。。（下同）
    mdict["two"] = 2
    mdict["three"] = 3
    print(mdict)   # {'three': 3, 'one': 1, 'two': 2}
