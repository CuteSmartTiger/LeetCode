#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 19:10
# @Author  : liuhu
# @Site    : 
# @File    : test_dp.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import unittest

from 动态规划.LeetCode62不同的路径一 import uniquePaths, unique_Paths


class TestDP(unittest.TestCase):
    def setUp(self):
        pass

    def test_uniquePaths(self):
        self.assertEqual(3, uniquePaths(3, 2))
        self.assertEqual(28, uniquePaths(7, 3))

    def test_unique_Paths(self):
        self.assertEqual(3, unique_Paths(3, 2))
        self.assertEqual(28, unique_Paths(7, 3))
        self.assertEqual(28, unique_Paths(3, 7))
