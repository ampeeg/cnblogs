# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 下午6:44
# @Author  : Clarence_Liao
# @FileName: L3_globals.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/


'''
    使用globals函数找出当前的全局号。其返回的是字典格式
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
    # 测试
    promos = [globals()[name] for name in globals()
              if name.endswith("Promo")]

    print(promos)   #  找到了三个策略函数 [<function FivePromo at 0x10c363b70>, <function TwoPromo at 0x10c363ae8>, <function VipPromo at 0x10abd3048>]

    def best_stratety(order):
        return max(promo(order) for promo in promos)



    ann = Customer('Ann Smith', 1)  # 会员

    # 创建购物车
    clothing = [Clothing('pants', 6, 200),
                Clothing('skirt', 1, 150),
                Clothing('shoes', 2, 230)]
    clothing.extend([Clothing('shirt', 1, 90), Clothing('bra', 2, 130)])

    print(Order(ann, clothing, best_stratety))  #<Order total: 2160.00 due: 1728.00>
