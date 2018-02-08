# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 下午10:40
# @Author  : Clarence_Liao
# @FileName: L1_namedtuple.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

# 导入可命名元组
from collections import namedtuple

# 创建的两种方法    （创建股票模型，每只股票包括name和price）

Stock_1 = namedtuple("stock", ("name", "price"))  # 方法1：第二个参数传入可迭代对象（元组、数组等都可）

Stock_2 = namedtuple("stock", "name price")       # 方法2：字符串之间用空格隔开

# 生成多只股票
stock01 = Stock_1("SH000001", 1)
stock02 = Stock_1("SH000002", 12)
stock03 = Stock_1("SH000003", 123)
stock04 = Stock_1("SH000004", 1234)

# 访问股票信息
print(stock01.name)     # 属性形式     SH000001
print(stock04[1])       # 列表形式     1234

