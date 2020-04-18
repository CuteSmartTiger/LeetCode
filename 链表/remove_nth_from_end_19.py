#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 22:38
# @Author  : liuhu
# @Site    : 
# @File    : remove_nth_from_end_19.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head, n):
    # 对空的判断
    if not head:
        return head
    pre_head = ListNode(0)
    pre_head.next = head
    left = right = pre_head

    # 相距n
    while n:
        right = right.next
        n -= 1

    while right and right.next:
        left = left.next
        right = right.next

    # while循环时对right.next判断
    # 是防止K为0时 此处删除节点报错
    left.next = left.next.next
    return pre_head.next
