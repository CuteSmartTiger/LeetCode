#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:45
# @Author  : liuhu
# @File    : 0344-字符串反转.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        if len(s) % 2 == 0:
            totalSwaps = int(len(s) / 2)
        else:
            totalSwaps = int((len(s) - 1) / 2)

        while totalSwaps > 0:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            totalSwaps -= 1