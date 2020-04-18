#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 23:28
# @Author  : liuhu
# @Site    : 
# @File    : merge_k_list_23.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 堆排序
from heapq import heappush, heappop


def merge_k_lists(lists):
    head = []
    for index, l in enumerate(lists):
        if l:
            heappush(head, (l.val, index))
            lists[index] = l.next  # 注意更新对列表中对应索引的值

    pre_head = cur = ListNode(-1)
    while head:
        val, i = heappop(head)
        cur.next = ListNode(val)
        cur = cur.next
        if lists[i]:
            heappush(head, (lists[i].val, i))
            lists[i] = lists[i].next  # 注意更新对列表中对应索引的值
    return pre_head.next


# 分冶法
# 首先合并两个链表的法已知，merge_two_link_lists
# 然后分而治之merge
def merge_two_link_lists(l1, l2):
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

    return pre_head.next


def merge(lists, left, right):
    # 分冶法
    if left == right:
        return lists[left]
    mid = left + (right - left) // 2
    l1 = merge(lists, left, mid)
    l2 = merge(lists, mid + 1, right)
    return merge_two_link_lists(l1, l2)


def merge_k_lists_2(lists):
    if not lists:
        return
    n = len(lists)
    return merge(lists, 0, n - 1)
