#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:13
# @Author  : liuhu
# @Site    : 
# @File    : reverse_list_206.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Methods(object):
    @classmethod
    def methods(cls):
        test_methods = []
        append = test_methods.append
        for attr in dir(cls):
            if attr.startswith("__") or attr.endswith("__") or attr == 'methods':
                continue
            if callable(getattr(cls, attr)):
                append(attr)
        return test_methods


class Solution(Methods):
    def reverse_list(self, head):
        if not head or not head.next:
            return head

        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        new_head = None
        while stack:
            if new_head is None:
                new_head = stack.pop()
                cur = new_head
            else:
                cur.next = stack.pop()
                cur = cur.next
        cur.next = None

        return new_head

    def reverse_list_recursion(self, head):
        print('进入递归中。。。。。')
        if not head or not head.next:
            print('递归出口')
            return head
        print('仍在递归中。。。。。')
        p = self.reverse_list_recursion(head.next)
        print('函数返回')
        head.next.next = head
        head.next = None
        return p

    def reverse_list_local(self, head):
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        return pre


class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex

    def output(self):
        output = []
        append = output.append
        cur = self
        while cur:
            append(cur.val)
            cur = cur.next
        return output


import unittest


class TestSolution(unittest.TestCase):
    node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node2 = ListNode(1)
    node3 = None

    def setUp(self):
        self.s = Solution()
        self.nodes = [self.node1, self.node2, self.node3]

    def test_methods(self):
        from itertools import product
        from copy import deepcopy
        for method, node in product(self.s.methods(), self.nodes):
            test_node = deepcopy(node)
            n = getattr(self.s, method)(test_node)
            if n:
                print(n.output())
            else:
                print(n)
