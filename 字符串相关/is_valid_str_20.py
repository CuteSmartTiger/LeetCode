#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 22:36
# @Author  : liuhu
# @Site    : 
# @File    : is_valid_str_20.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 利用栈
def is_valid(s):
    if not str:
        return True
    stack = []
    s_match = {'(': ')', '{': '}', '[': ']', ')': '(', '}': '{', ']': '['}
    for i, v in enumerate(s):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s_match[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])

    return False if stack else True
