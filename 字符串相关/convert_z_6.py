#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 22:24
# @Author  : liuhu
# @Site    : 
# @File    : convert_z_6.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def convert(s, numRows):
    if numRows < 2:
        return s

    s_nums = ['' for _ in range(numRows)]
    i = 0
    flag = -1
    for c in s:
        s_nums[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag

    return ''.join(s_nums)
