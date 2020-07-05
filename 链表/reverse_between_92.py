#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 0:01
# @Author  : liuhu
# @Site    : 
# @File    : reverse_between_92.py
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

    @staticmethod
    def reverse_between(head, m, n):
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


import unittest


class TestSolution(unittest.TestCase):
    node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node2 = None

    def setUp(self):
        self.s = Solution()
        self.nodes_input_to_output = [
            (self.node1, 2, 4, [1, 4, 3, 2, 5]),
            (self.node1, 2, 2, [1, 2, 3, 4, 5]),
            (self.node1, 1, 1, [1, 2, 3, 4, 5]),
            (self.node2, 1, 2, None),
        ]

    def test_methods(self):
        from itertools import product
        from copy import deepcopy
        for method, (node, m, n, output) in product(self.s.methods(), self.nodes_input_to_output):
            test_node = deepcopy(node)
            n = getattr(self.s, method)(test_node, m, n)
            if n:
                self.assertEqual(n.output(), output)
                print(n.output(), output)
            else:
                print(n)
