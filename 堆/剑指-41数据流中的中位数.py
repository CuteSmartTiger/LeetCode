#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 22:46
# @Author  : liuhu
# @Site    : 
# @File    : 剑指-41数据流中的中位数.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import heapq


class MedianFinder(object):
    def __init__(self):
        self.len = 0
        self.min_heap, self.max_heap = [], []

    def addNum(self, num):
        self.len += 1
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self):
        if self.len & 1 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        return self.min_heap[0]
