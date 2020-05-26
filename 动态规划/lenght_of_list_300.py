#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 22:15
# @Author  : liuhu
# @Site    : 
# @File    : lenght_of_list_300.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:

    @staticmethod
    def length_of_list_binary(nums):
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l < r:
                    mid = l + (r - l) // 2
                    if d[mid] < n:
                        l = mid + 1
                    elif d[mid] > n:
                        r = mid
                    else:
                        loc = mid
                        break
                d[loc] = n
        return len(d)

    @staticmethod
    def length_of_list(nums):
        # 动态规划  dp 代表以nums[i]结尾的
        # 递增子序列的长度
        if not nums:
            return 0
        dp = [1]
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


from unittest import TestCase


class TestLengthOfList(TestCase):
    def setUp(self):
        self.s = Solution()
        self.nums_to_res = (
            # ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([4, 10, 4, 3, 8, 9], 3),
        )

    def test_all_functions(self):
        for heights, res in self.nums_to_res:
            self.assertEqual(self.s.length_of_list_binary(heights), res)
