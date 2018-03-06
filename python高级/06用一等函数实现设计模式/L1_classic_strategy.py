# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 下午3:07
# @Author  : Clarence_Liao
# @FileName: L1_classic_strategy.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    经典的策略模式:
        封装一系列可以互相替代的算法，使得算法可以独立与使用它的客户而变化。


    假设当代商城某服装店有以下三种打折规则：
        1、对于会员，全部商品8.5折
        2、同一件商品买两件及以上，除第一件外，剩余的7.5折
        3、买上5件不同商品，全部商品打8折
    三种规则只能享受一个。
'''


from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name vip')     # 消费者对象


class Clothing:                # 服装类

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 订单类

    def __init__(self, customer, clothing, promotion=None):
        self.customer = customer
        self.clothing = list(clothing)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.clothing)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 创建三种折扣的基类

    @abstractmethod
    def discount(self, order):
        ''':returns 计算折扣'''


class VipPromo(Promotion):  # 会员折扣
    """:returns 会员8.5折"""

    def discount(self, order):
        return order.total() * .15 if order.customer.vip  else 0


class TwoPromo(Promotion):  # 第二个
    ''':returns 同一件衣服两件以上，第二件及之后的7.5折'''

    def discount(self, order):
        discount = 0
        for item in order.clothing:
            if item.quantity >= 2:
                discount += (item.total() - item.price) * .25
        return discount


class FivePromo(Promotion):  # 5种以上
    """ :returns 买5种不同服装以上，每件8折"""

    def discount(self, order):
        distinct_items = {item.name for item in order.clothing}
        if len(distinct_items) >= 5:
            return order.total() * .2
        return 0


if __name__ == "__main__":
    # 创建消费者
    joe = Customer('John Doe', 0)  # 非会员
    ann = Customer('Ann Smith', 1) # 会员

    # 创建购物车
    clothing = [Clothing('pants', 6, 200),
                Clothing('skirt', 1, 150),
                Clothing('shoes', 2, 230)]
    print(Order(joe, clothing, VipPromo()))  #   <Order total: 1810.00 due: 1810.00>    不是会员，不打折
    print(Order(ann, clothing, VipPromo()))  #   <Order total: 1810.00 due: 1538.50>    会员，打85折


    print(Order(joe, clothing, TwoPromo()))  # <Order total: 1810.00 due: 1502.50>   两件以上7.5折
    print(Order(joe, clothing, FivePromo())) # <Order total: 1810.00 due: 1810.00>   没到5种不打折

    clothing.extend([Clothing('shirt', 1, 90), Clothing('bra', 2, 130)])
    print(Order(joe, clothing, FivePromo())) # <Order total: 2160.00 due: 1728.00>  刚好5种打8折


