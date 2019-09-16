#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 10:59
# @Author  : liuhu
# @Site    : 
# @File    : 不用加减乘除符号做加法.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def plus(a, b):
    while True:
        if a < 0 and abs(a) < b:
            sum = a ^ b
        else:
            sum = a ^ b
        carry = (a & b) << 1
        if carry == 0:
            break
        else:
            a = sum
            b = carry
    return sum


# print(plus(0, 3))
# print(plus(5, -7))
# print(plus(99, 199))
# print(plus(2, -3))
# print(plus(-2, 3))
# print(plus(3, -2))
print(plus(-5, 8))
# print(plus(-3, 2))
