#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 22:24
# @Author  : liuhu
# @Site    : 
# @File    : 零钱兑换I.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 题目：一个数组包含正数的硬币,比如可选币值为
# coins，目标值为T，问总共有多少种方法

coins = [1, 2, 5, 10]
T = 10


class Coins(object):

    def get_coins(self, available_coins, target):
        if not available_coins or target < 0:
            return 0
        return self.processes(available_coins, 0, target)

    def processes(self, coins, index, target):
        res = 0
        if index == len(coins):
            if target == 0:
                return 1
            elif target != 0:
                return 0
        else:
            i = 0
            while coins[index] * i <= target:
                res += self.processes(coins, index + 1, target - coins[index] * i)
                i += 1
        return res


if __name__ == '__main__':
    c = Coins()
    print(c.get_coins(coins, 0))
    print(c.get_coins(coins, 1))
    print(c.get_coins(coins, 2))
    print(c.get_coins(coins, 5))
    print(c.get_coins(coins, 10))
    pass

import unittest


class TestCoins(unittest.TestCase):
    def setUp(self):
        self.c = Coins()
        self.coins = coins

    def test_coins(self):
        print(self.c.get_coins(self.coins, 0))
        self.assertEqual(self.c.get_coins(self.coins, 0), 2)
        print(self.c.get_coins(self.coins, 10))
        # self.assertEqual(get_coins())
