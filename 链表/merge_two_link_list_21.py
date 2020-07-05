#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 22:47
# @Author  : liuhu
# @Site    : 
# @File    : merge_two_link_list_21.py
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
    def merge_two_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2

    def merge_two_lists_recursion_improve(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_two_lists_recursion_improve(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists_recursion_improve(l1, l2.next)
            return l2

    def merge_two_lists_iter(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
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

        return dummy.next

    def merge_two_lists_iter_improve(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 is not None else l2

        return dummy.next


import unittest


class TestSolution(unittest.TestCase):
    node1 = ListNode(1, ListNode(2, ListNode(4, )))
    node2 = ListNode(1, ListNode(3, ListNode(4, )))

    def setUp(self):
        self.s = Solution()
        self.nodes_input_to_output = [
            (self.node1, self.node2, [1, 1, 2, 3, 4, 4]),
            (self.node1, None, [1, 2, 4, ]),
            (None, None, None),
        ]

    def test_methods(self):
        from itertools import product
        from copy import deepcopy
        for method, (l1, l2, output) in product(self.s.methods(), self.nodes_input_to_output):
            test_node1 = deepcopy(l1)
            test_node2 = deepcopy(l2)
            n = getattr(self.s, method)(test_node1, test_node2)
            if n:
                self.assertEqual(n.output(), output)
                print(n.output(), output)
            else:
                print(n)
