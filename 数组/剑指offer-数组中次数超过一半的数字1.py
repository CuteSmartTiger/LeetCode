#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 22:16
# @Author  : liuhu
# @Site    : 
# @File    : 剑指offer-数组中次数超过一半的数字1.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

test_list = [1, 2, 3, 4, 2, 6, 3, 2, 2, 2, 4, 2, 2]


def find_more_than_half_num(nums):
    if not nums or len(nums) == 1:
        return None
    result = nums[0]
    time = 1
    n = len(nums)
    for i in range(1, n):
        if not time:
            result = nums[i]
            time = 1
        if nums[i] == result:
            time += 1
        else:
            time -= 1
    return result

print(find_more_than_half_num(test_list))