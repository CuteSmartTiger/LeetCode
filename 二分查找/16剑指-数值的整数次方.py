#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 17:47
# @Author  : liuhu
# @Site    : 
# @File    : 16剑指-数值的整数次方.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def power_exponent(base, n):
    if n == 0:
        return 1
    if n == 1:
        return base
    result = power_exponent(base, n >> 1)
    result *= result
    if n & 1 == 1:
        result *= base
    return result


print(power_exponent(2, 3))
print(power_exponent(-2, 4))
print(power_exponent(2, 0))
# print(power_exponent(4, 0.5))
