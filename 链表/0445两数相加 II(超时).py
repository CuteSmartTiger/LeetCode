#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 16:44
# @Author  : liuhu
# @File    : 0445两数相加 II(超时).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l1 = l2.next
        head = ListNode(-1)
        flag = 0
        while stack1 and stack2:
            val1 = stack1.pop()
            val2 = stack2.pop()
            temp = val1 + val2 + flag
            if temp >= 10:
                save = temp - 10
                flag = 1
            else:
                save = temp
                flag = 0
            if not head.next:
                head.next = ListNode(save)
            else:
                new_node = ListNode(save)
                new_node.next = head.next
                head.next = new_node
        while stack1:
            val1 = stack1.pop()
            temp = val1 + flag
            if temp >= 10:
                save = temp - 10
                flag = 1
            else:
                save = temp
                flag = 0
            new_node = ListNode(save)
            new_node.next = head.next
            head.next = new_node

        while stack2:
            val2 = stack2.pop()
            temp = val2 + flag
            if temp >= 10:
                save = temp - 10
                flag = 1
            else:
                save = temp
                flag = 0

            new_node = ListNode(save)
            new_node.next = head.next
            head.next = new_node

        if flag == 1:
            new_node = ListNode(1)
            new_node.next = head.next
            head.next = new_node

        return head.next