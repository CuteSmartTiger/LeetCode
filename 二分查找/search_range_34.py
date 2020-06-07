#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 10:27
# @Author  : liuhu
# @Site    : 
# @File    : search_range_34.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 利用二分查找搜索左右边界
class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        return self.search_left(nums, target), self.search_right(nums, target)

    def search_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid - 1
        if left > len(nums) - 1 or nums[left] != target:
            return -1
        return left

    def search_right(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        return self.search_index(nums, target, -1), self.search_index(nums, target, 1)

    def search_index(self, nums, target, direction=1):
        """-1 means search left,1 means search right"""
        if direction not in (1, -1):
            raise ValueError('direction could only be -1 or 1')
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if direction == -1:
                    right = mid - 1
                else:
                    left = mid + 1
        if direction == -1:
            if left > len(nums) - 1 or nums[left] != target:
                return -1
            return left
        else:
            if right < 0 or nums[right] != target:
                return -1
            return right