#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 21:17
# @Author  : liuhu
# @Site    : 
# @File    : two_sum_1.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def two_sum(nums, target):
    target_dict = {}
    for index,value in enumerate(nums):
        if value not in target_dict:
            target_dict[target-value]=index
        else:
            return [target_dict[value],index]
    return None


import unittest


class TestWays(unittest.TestCase):
    def setUp(self):
        self.nums1 = [2, 7, 9, 11, 15]
        self.target1 = 9

    def test_num_ways(self):
        self.assertEqual(two_sum(self.nums1,self.target1), [0,1])
