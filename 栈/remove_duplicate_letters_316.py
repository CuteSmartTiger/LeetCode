#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 19:25
# @Author  : liuhu
# @Site    : 
# @File    : remove_duplicate_letters.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def remove_duplicate_letters(s):
    visited = set()
    last_index = {c: i for i, c in enumerate(s)}
    stack = []
    for index, value in enumerate(s):
        if value not in visited:
            while stack and value < stack[-1] and index < last_index[stack[-1]]:
                visited.discard(stack.pop())

            visited.add(value)
            stack.append(value)
    return ''.join(stack)
