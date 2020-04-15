#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:13
# @Author  : liuhu
# @Site    : 
# @File    : reverse_list_206.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def reverse_list(head):
    # 边界条件的考虑 空或者一个返回
    if not head or not head.next:
        return head

    # 原地反转
    pre = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    return pre

# 方法二 递归
