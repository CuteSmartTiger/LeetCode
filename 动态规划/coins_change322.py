#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 22:44
# @Author  : liuhu
# @Site    : 
# @File    : coins_change322.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Coins(object):
    def coin_change(self, coins, amount):

        # 基础问题
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        res = float('INF')
        for coin in coins:
            sub = self.coin_change(coins, amount - coin)
            # 子问题无解，跳过
            if sub == -1:
                continue
            res = min(res, 1 + sub)
        return res if res != float('INF') else -1

    def coin_change_mem(self, coins, amount, mem=None):
        if mem is None:
            mem = {}
        if amount in mem:
            return mem[amount]
        # 基础问题
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        res = float('INF')
        for coin in coins:
            sub = self.coin_change_mem(coins, amount - coin, mem=mem)
            # 子问题无解，跳过
            if sub == -1:
                continue
            res = min(res, 1 + sub)
        mem[amount] = res if res != float('INF') else -1
        return mem[amount]

    def test_coins_change_dp(self, coins, amount):
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) coins[j]为所有硬币

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i - c] + 1, dp[i])
        return dp[-1] if dp[-1] != float("inf") else -1


import unittest


class TestCoins(unittest.TestCase):
    def setUp(self):
        self.c = Coins()
        self.coins = [1, 2, 5]
        self.amount = 11

    def test_coins_change(self):
        self.assertEqual(self.c.coin_change(self.coins, self.amount), 3)

        self.coins = [2]
        self.amount = 3
        self.assertEqual(self.c.coin_change(self.coins, self.amount), -1)

    def test_coins_change_mem(self):
        self.assertEqual(self.c.coin_change_mem(self.coins, self.amount), 3)

        self.coins = [2]
        self.amount = 3
        self.assertEqual(self.c.coin_change_mem(self.coins, self.amount), -1)

    def test_coins_change_dp(self):
        self.assertEqual(self.c.test_coins_change_dp(self.coins, self.amount), 3)

        self.coins = [2]
        self.amount = 3
        self.assertEqual(self.c.test_coins_change_dp(self.coins, self.amount), -1)

# 优化方向 一是计算时间  二是计算空间
