#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 17:51
# @Author  : liuhu
# @Site    : 
# @File    : length_of_longest_sub_string.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 利用集合维护一个队列
def length_of_longest_substring(s):
    if not s:
        return 0
    n = len(s)
    max_len = 0
    cur_len = 0
    window_set = set()
    left = 0
    for i in range(n):
        cur_len += 1

        # 将已将出现的字符之前的所有字符移除
        while s[i] in window_set:
            window_set.remove(s[left])
            left += 1
            cur_len -= 1

        if cur_len > max_len:
            max_len = cur_len
        window_set.add(s[i])
    return max_len
