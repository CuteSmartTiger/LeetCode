#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 22:48
# @Author  : liuhu
# @Site    : 
# @File    : top_k_freq_347.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 时间复杂度 : O(Nlogk)。
# 空间复杂度 : {O(k)，用于存储堆元素
# 用python内置堆函数
def top_k_frequent(nums, k):
    freq_dict = {}
    for num in nums:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

    import heapq
    h_list = []

    for key, value in freq_dict.items():
        if k > 0:
            heapq.heappush(h_list, (value, key))
            k = k - 1
            continue
        else:
            h_v, h_k = heapq.heappop(h_list)
            if value > h_v:
                heapq.heappush(h_list, (value, key))
            else:
                heapq.heappush(h_list, (h_v, h_k))

    return [x[1] for x in h_list]
