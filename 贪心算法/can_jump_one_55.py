#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 21:04
# @Author  : liuhu
# @Site    : 
# @File    : can_jjump_I.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def can_jump(nums):
    if not isinstance(nums, list) or not nums:
        raise ValueError('nums must be list or  cannot be []')
    # 遍历数组中每一个点，判断此位置可以到达的最远位置
    # 最远元素的索引位置
    n = len(nums) - 1

    # 可达到的最远位置，初始化为0
    max_location = 0
    # 当前索引位置
    cur = 0
    while cur <= max_location:
        max_location = max(max_location, nums[cur] + cur)
        cur += 1
        if max_location >= n:
            return True

    return False


import unittest


class TestWays(unittest.TestCase):
    def setUp(self):
        self.nums_one = [2, 3, 1, 1, 4, 5]
        self.nums_two = [3, 2, 1, 0, 4, 5]

    def test_num_ways(self):
        self.assertTrue(can_jump(self.nums_one))
        self.assertFalse(can_jump(self.nums_two))
