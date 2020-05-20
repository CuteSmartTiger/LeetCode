#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 22:15
# @Author  : liuhu
# @Site    : 
# @File    : unique_paths_I_62.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:
    @staticmethod
    def unique_paths_three(m, n):
        if m < 1 or n < 1:
            raise ValueError('m or n must > 0')
        if not isinstance(m, int) or not isinstance(n, int):
            raise ValueError('m or n must be int ')
        # 空间复杂度优化到n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # pre[j]是等于cur[j]
                # cur[j] = cur[j] + cur[j-1]
                cur[j] += cur[j - 1]

        return cur[-1]

    @staticmethod
    def unique_paths_two(m, n):
        # 空间复杂度  优化到2n
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            # 更新 pre
            pre = cur[:]

        return cur[-1]

    @staticmethod
    def unique_paths_one(m, n):
        # 动态规划 初始dp table
        row = [None for _ in range(n)]
        dp = []
        for _ in range(m):
            dp.append(row)

        # 初始化
        for i in range(n):
            dp[0][i] = 1

        for j in range(m):
            dp[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


from unittest import TestCase


class TestUniquePath(TestCase):
    def setUp(self):
        self.s = Solution()
        self.m_n_res = [
            ((3, 2), 3),
            ((7, 3), 28),
            # ((0, 2), 0)
        ]

    def test_(self):
        for m_n, res in self.m_n_res:
            self.assertEqual(self.s.unique_paths_three(*m_n), res)
