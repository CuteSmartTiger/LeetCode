#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 23:33
# @Author  : liuhu
# @Site    : 
# @File    : min_distance_72.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:

    @staticmethod
    def min_distance(word1, word2):
        # 优化下代码
        m = len(word1)
        n = len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, m + 1):
            dp[0][i] = i

        for j in range(1, n + 1):
            dp[j][0] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[-1][-1]

    @staticmethod
    def min_distance_two(word1: str, word2: str) -> int:
        # 时间复杂度O(M*N)
        # 空间复杂度O(M*N)
        m = len(word1)
        n = len(word2)

        if not m:
            return n
        if not n:
            return m

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for c in range(m + 1):
            dp[0][c] = c

        for r in range(n + 1):
            dp[r][0] = r

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[-1][-1]
