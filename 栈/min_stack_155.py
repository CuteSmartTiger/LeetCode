#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 15:57
# @Author  : liuhu
# @Site    : 
# @File    : min_stack_155.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.m_v = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.m_v:
            self.m_v.append(x)
        else:
            value = self.m_v[-1]
            self.m_v.append(min(x, value))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.m_v.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.m_v:
            return self.m_v[-1]
