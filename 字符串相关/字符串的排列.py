#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 12:00
# @Author  : liuhu
# @File    : 字符串的排列.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    cout=0
    s3= ''.join(list(reversed(s1)))
    if s1  in s2:
        cout +=1
    if s3 in s2:
        cout +=1
    if cout:
        return True
    return False


s1 = "ab"
s2 = "   eidboaoo   "
print s2.strip()
print checkInclusion(s1, s2)
