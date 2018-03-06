# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 下午6:11
# @Author  : Clarence_Liao
# @FileName: L2_func_strategy.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    下面使用函数完成"经典"策略
'''

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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())



def VipPromo(order):  # 会员折扣
    return order.total() * .15 if order.customer.vip  else 0


def TwoPromo(order):  # 第二个
    discount = 0
    for item in order.clothing:
        if item.quantity >= 2:
            discount += (item.total() - item.price) * .25
    return discount


def FivePromo(order):  # 5种以上
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
    print(Order(joe, clothing, VipPromo))  #   <Order total: 1810.00 due: 1810.00>    不是会员，不打折
    print(Order(ann, clothing, VipPromo))  #   <Order total: 1810.00 due: 1538.50>    会员，打85折


    print(Order(joe, clothing, TwoPromo))  # <Order total: 1810.00 due: 1502.50>   两件以上7.5折
    print(Order(joe, clothing, FivePromo)) # <Order total: 1810.00 due: 1810.00>   没到5种不打折

    clothing.extend([Clothing('shirt', 1, 90), Clothing('bra', 2, 130)])
    print(Order(joe, clothing, FivePromo)) # <Order total: 2160.00 due: 1728.00>  刚好5种打8折

    promos = [VipPromo, TwoPromo, FivePromo]


    def best_stratety(order):
        return max(promo(order) for promo in promos)


    print(Order(joe, clothing, best_stratety))   # <Order total: 2160.00 due: 1728.00>  自动选择最优的策略


