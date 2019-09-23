#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 11:28
# @Author  : liuhu
# @Site    : 
# @File    : LeetCode25k个一组反转链表(栈的方法).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dumy = ListNode(-1)
        pre = dumy
        while True:
            count = k
            cur = head
            stack = []
            while count and cur:
                stack.append(cur)
                cur = cur.next
                count -= 1
            if count:
                pre.next = head
                break

            while stack:
                pre.next = stack.pop()
                pre = pre.next

            pre.next = cur
            head = cur
        return dumy.next