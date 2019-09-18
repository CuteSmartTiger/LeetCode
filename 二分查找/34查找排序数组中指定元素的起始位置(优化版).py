#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 21:48
# @Author  : liuhu
# @Site    : 
# @File    : 34查找排序数组中指定元素的起始位置.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# left < right, 执行完毕输出
# left <= right, 执行中判断输出


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        left = self.find_first(nums, target)
        right = self.find_last(nums, target)
        return [left, right]

    def find_last(self, nums, target):
        n = right = len(nums) - 1
        left = 0

        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if mid < n:
                    if nums[mid + 1] == target:
                        left = mid + 1
                    else:
                        return mid
                else:
                    return mid
        return -1

    def find_first(self, nums, target):
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid > 0:
                    if nums[mid - 1] == target:
                        right = mid - 1
                    else:
                        return mid
                else:
                    return mid
        return -1

