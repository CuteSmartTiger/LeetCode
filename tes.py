#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 0:03
# @Author  : liuhu
# @Site    : 
# @File    : tes.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def containsNearbyDuplicate(nums,k):
    n = len(nums)
    j = 0
    while j <= n - k - 1:
        tes = set(nums[j:k + j + 1])
        if len(tes) < k:
            return True
        else:
            j += 1
    return False

# li = [1,2,3,1]
li = [99,99]
k =2

print(containsNearbyDuplicate(li,k))