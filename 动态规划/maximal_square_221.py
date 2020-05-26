#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 20:59
# @Author  : liuhu
# @Site    : 
# @File    : maximal_square_221.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:

    @staticmethod
    def maximal_square(matrix):
        # dp 动态规划
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_side = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    continue
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        max_square = max_side * max_side
        return max_square


from unittest import TestCase


class TestMaxSquare(TestCase):
    def setUp(self):
        self.matrix = [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]
        ]
        self.s = Solution()

    def test_max_square(self):
        self.assertEqual(self.s.maximal_square(self.matrix), 4)
