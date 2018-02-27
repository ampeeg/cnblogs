# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 下午11:11
# @Author  : Clarence_Liao
# @FileName: L4_dict_2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

'''
    字典推导式：字典推导式的创建方法同列表推导式类似

    以下直接引用《流畅的python》中的例子
'''


if __name__ == "__main__":
    DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code)   # {'Russia': 7, 'Indonesia': 62, 'Brazil': 55, 'China': 86, 'India': 91, 'Bangladesh': 880, 'Pakistan': 92, 'United States': 1, 'Nigeria': 234, 'Japan': 81}

    code_upper = {code: country.upper() for country, code in country_code.items() if code < 66}
    print(code_upper)     # {1: 'UNITED STATES', 7: 'RUSSIA', 62: 'INDONESIA', 55: 'BRAZIL'}