#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 22:39
# @Author  : liuhu
# @Site    : 
# @File    : 33_search.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 当起始位置到mid之间不包含旋转点时，有序
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    # 当target在之间时，不断向前规约
                    r = mid - 1
                else:
                    # 当target大于nums[mid]时，在mid到len(nums)-1之间，需要向后规约
                    # 当target小于nums[0]时，在mid到len(nums)-1之间，需要向后规约
                    l = mid + 1
            else:  # nums[0] >  nums[mid]
                # 当起始位置到mid之间包含旋转点时，即mid到len(nums) - 1有序
                # 当target在有序直接时，向后规约
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    # 若target小于nums[mid]则，向前规约查找
                    # 若target大于nums[len(nums) - 1]，即target>=nums[0]则依然向前规约查找
                    r = mid - 1
        return -1

    def simplify_search(self, nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 总结上面向前规约的三种情况：
            # 1. nums[0] <= target < nums[mid]
            # 2. target < nums[mid] < nums[0]
            # 3.  nums[mid] < nums[0] <= target
            # 这三个是互斥的，同时只要有一个为真则向前规约
            # 如下：
            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                r = mid - 1
            else:
                l = mid +1
        return -1


import unittest


class TestRotateRight(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.test_nums_to_res = (
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1)
        )

    def test_search(self):
        for nums, target, res in self.test_nums_to_res:
            self.assertEqual(self.s.search(nums, target), res)
            self.assertEqual(self.s.simplify_search(nums, target), res)
