#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 23:54
# @Author  : liuhu
# @Site    : 
# @File    : climb_stairs_70.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:
    @staticmethod
    def climb_stairs(n):
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    @staticmethod
    def climb_stairs(n):
        a, b = 1, 0
        while n:
            a, b = a + b, a
            n -= 1
        return a
