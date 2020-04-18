#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 22:47
# @Author  : liuhu
# @Site    : 
# @File    : merge_two_link_list_21.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    pre_head = cur = ListNode(-1)
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    if l1:
        cur.next = l1

    if l2:
        cur.next = l2

    # cur.next = l1 if l1 is not None else l2

    return pre_head.next


# 递归的方法
def merge_two_lists_recursion(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        l1.next = merge_two_lists_recursion(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_recursion(l2.next, l1)
        return l2
