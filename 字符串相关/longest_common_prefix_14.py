#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:49
# @Author  : liuhu
# @File    : 0014最长公共前缀.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 利用zip
def longest_common_prefix(strs):
    if not strs:
        return ''
    res = ''
    for tem in zip(*strs):
        if len(set(tem)) == 1:
            res += tem[0]
        else:
            break
    return res


# 按字典排序数组，比较第一个，和最后一个单词
def longest_common_prefix_by_sort(strs):
    if not strs:
        return ''

    strs.sort()
    start = strs[0]
    end = strs[-1]
    for i, s in enumerate(start):
        if start[i] == end[i]:
            continue
        else:
            break
    return start[:i]


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    min_n = -1
    for m in strs:
        n = len(m)
        if min_n == -1:
            min_n = n
        if n < min_n:
            min_n = n

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

        if not mark:
            j += 1
    if not first[0:j]:
        return ''
    return first[0:j]
