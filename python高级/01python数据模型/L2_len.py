# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 下午11:47
# @Author  : Clarence_Liao
# @FileName: L2_len.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


class Foo:
    def __len__(self):            # 重写__len__方法
        print("method __len__")
        return 1


if __name__ == "__main__":
    foo = Foo()
    n = len(foo)        # 使用len()时会自动调用__len__方法：method __len__
    print(n)            # 1