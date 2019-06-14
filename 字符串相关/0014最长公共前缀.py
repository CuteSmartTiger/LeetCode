#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:49
# @Author  : liuhu
# @File    : 0014最长公共前缀.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    min_n=-1
    for m in strs:
        print min_n
        n = len(m)
        if min_n == -1:
            min_n = n
        if n < min_n:
            min_n = n

    print min_n
    if not min_n:
        return ''
    mark = False
    j = 0
    first = strs[0]
    while not mark:
        compare = first[j]
        for num in strs:
            if num[j] != compare:
                mark = True
                break
        print j
        if not mark:
            j += 1
    print j
    if not first[0:j]:
        return ''
    return first[0:j]


s = ["flower", "flow", "flight"]
# print longestCommonPrefix(s)
print longestCommonPrefix(["","b"])
