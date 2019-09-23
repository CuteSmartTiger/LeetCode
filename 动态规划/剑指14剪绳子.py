#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 20:58
# @Author  : liuhu
# @Site    : 
# @File    : 剑指14剪绳子.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def max_cutting_solution(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    location = [0 if i >=4 else i for i in range(n + 1)]

    for i in range(4, n + 1):
        max = 0
        for j in range(1, i // 2 + 1):
            loc = location[j] * location[i - j]
            if loc > max:
                max = loc
            location[i] = max
    return location[-1]


# print(max_cutting_solution(1))
# print(max_cutting_solution(2))
# print(max_cutting_solution(3))
print(max_cutting_solution(4))