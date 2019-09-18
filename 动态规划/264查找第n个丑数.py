#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 22:31
# @Author  : liuhu
# @Site    : 
# @File    : 264查找第n个丑数.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 丑数数列的初始化,第一个丑数是1
        dp = [1]
        # 三个分别乘2,3,5的指针
        i2 = i3 = i5 = 0
        while n > 1:  # 在丑数dp数组中加入n-1个丑数后，停止,此时列表最后一个为第N个丑数
            # 取三个指针对应相乘后的最小值
            # 若要加入的最小丑数是*2过来的，则*2的指针+1，即指向下一个丑数
            # 针对每一个都要判断，以便相同的丑数只添加一次到dp列表中
            tmp = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if tmp == dp[i2] * 2:
                i2 += 1
            if tmp == dp[i3] * 3:
                i3 += 1
            if tmp == dp[i5] * 5:
                i5 += 1
            dp.append(tmp)
            n -= 1
        return dp[-1]

    def nth_ugly_num(self, n):
        import heapq
        heap = [1]
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            res = heapq.heappop(heap)
            # 剔除相同的丑数，通过堆实现排序
            while heap and res == heap[0]:
                res = heapq.heappop(heap)

            a, b, c = res * 2, res * 3, res * 5
            for t in [a, b, c]:
                heapq.heappush(heap, t)
        return res

    def nth_ugly_number(self, n):
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            if dp[i] >= 2 * dp[l_2]:
                l_2 += 1
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]
