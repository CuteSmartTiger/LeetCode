#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 22:28
# @Author  : liuhu
# @Site    : 
# @File    : middle_node_876.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middle_node(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if not fast:
            return slow
        else:
            return slow.next
