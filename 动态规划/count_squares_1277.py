#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 22:07
# @Author  : liuhu
# @Site    : 
# @File    : count_squares_1277.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:
    @staticmethod
    def count_squares_purity(matrix):
        if not len(matrix) or not len(matrix[0]):
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        pre_row = matrix[0]
        res = sum(pre_row)
        for i in range(1, rows):
            cur_row = matrix[i]
            print('pre_row', pre_row)
            print('cur_row', cur_row)
            for j in range(cols):
                if j == 0:
                    pass
                    # cur_row[j]=matrix[i][j]
                else:
                    if matrix[i][j] == 0:
                        cur_row[j] = 0
                    else:
                        cur_row[j] = min(cur_row[j - 1], pre_row[j - 1], pre_row[j]) + 1
                res += cur_row[j]
            pre_row = cur_row
            print(cur_row)

        return res

    def countSquares(self, matrix):
        if not len(matrix) or not len(matrix[0]):
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                res += dp[i][j]
        return res


from unittest import TestCase


class TestMaxSquare(TestCase):
    def setUp(self):
        self.matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1],
        ]
        self.s = Solution()

    def test_max_square(self):
        self.assertEqual(self.s.count_squares_purity(self.matrix), 15)
