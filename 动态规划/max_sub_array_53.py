#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 21:23
# @Author  : liuhu
# @Site    : 
# @File    : max_sub_array_53.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:

    @staticmethod
    def max_sub_array_three(nums):
        if not nums:
            return None
        for index, num in enumerate(nums):
            if index == 0:
                pre = nums[0]
                res = pre
                continue
            cur = max(pre + num, num)
            if cur > res:
                res = cur
            pre = cur
        return res

    @staticmethod
    def max_sub_array_two(nums):
        # 在原有的数组上修改,节省空间复杂度
        if not nums:
            return
        for index, num in enumerate(nums):
            if index == 0:
                res = nums[0]
                continue
            nums[index] = max(nums[index - 1] + num, num)
            if res < nums[index]:
                res = nums[index]
        return res

    @staticmethod
    def max_sub_array_one(nums):
        # 不改变原有数组
        dp = []
        res = None
        for index, num in enumerate(nums):
            if index == 0:
                res = nums[0]
                dp.append(nums[0])
            else:
                dp.append(max(dp[index - 1] + num, num))
            if dp[index] > res:
                res = dp[index]

        return res


from unittest import TestCase


class TestMaxSubArray(TestCase):
    def setUp(self):
        self.s = Solution()
        self.arrays_res_tuple = [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([], None),
            ([0], 0)
        ]

    def test_max_sub_array_three(self):
        for arrays, res in self.arrays_res_tuple:
            self.assertEqual(self.s.max_sub_array_three(arrays),res)
