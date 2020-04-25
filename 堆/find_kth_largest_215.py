#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 21:53
# @Author  : liuhu
# @Site    : 
# @File    : find_kth_largest_215.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 使用python自带的小根堆包
def find_kth_largest(nums, k):
    import heapq
    h_list = []

    while k and nums:
        heapq.heappush(h_list, nums.pop())
        k -= 1
    while nums:
        nex = nums.pop()
        h_min = heapq.heappop(h_list)
        save = nex if nex > h_min else h_min
        heapq.heappush(h_list, save)
    return heapq.heappop(h_list)
