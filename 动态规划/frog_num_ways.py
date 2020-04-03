#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 23:19
# @Author  : liuhu
# @Site    : 
# @File    : 青蛙跳.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def num_ways_by_recursion(n):
    if n < 0:
        raise ValueError('n must >= 0')
    elif n == 0:
        return 1
    elif n in (1, 2):
        return n
    else:
        return num_ways_by_recursion(n - 1) + num_ways_by_recursion(n - 2)


def num_ways(n):
    a = b = 1
    for i in range(n):
        a, b = a + b, a
    return b


import unittest


class TestWays(unittest.TestCase):
    def setUp(self):
        pass

    def test_num_ways(self):
        self.assertEqual(num_ways(3), 3)

    def test_num_ways_by_recursion(self):
        self.assertEqual(num_ways_by_recursion(4), 5)
