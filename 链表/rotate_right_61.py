#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 23:26
# @Author  : liuhu
# @Site    : 
# @File    : rotate_right_61.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


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
    def rotate_right(self, head, k):
        if not head or not head.next:
            return head

        # 计算长度
        n = 1
        tail = head
        while tail and tail.next:
            n += 1
            tail = tail.next
        # tail 为链表的尾节点

        # 取模,计算要移动的节点数
        m = n - k % n

        # 取模为0时 不用旋转，此处做个优化
        if m == n:
            return head

        cur = head
        while m > 1:
            cur = cur.next
            m -= 1
        new_head = cur.next
        cur.next = None

        tail.next = head
        return new_head


import unittest


class TestSolution(unittest.TestCase):
    node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node2 = None
    node3 = ListNode(1)

    def setUp(self):
        self.s = Solution()
        self.nodes_input_to_output = [
            (self.node1, 3, [3, 4, 5, 1, 2]),
            (self.node1, 8, [3, 4, 5, 1, 2]),
            (self.node1, 1, [5,1, 2, 3, 4]),
            (self.node2, 1, None),
            (self.node3, 3, [1]),
        ]

    def test_methods(self):
        from itertools import product
        from copy import deepcopy
        for method, (node, k, output) in product(self.s.methods(), self.nodes_input_to_output):
            test_node = deepcopy(node)
            n = getattr(self.s, method)(test_node, k)
            if n:
                self.assertEqual(n.output(), output)
                print(n.output(), output)
            else:
                print(n)
