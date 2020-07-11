#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:04
# @Author  : liuhu
# @Site    : 
# @File    : delete_node_237.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

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
    def delete_node(self, head, node):
        if not head:
            return head

        if not node:
            return head

        dummy = Node(-1)
        dummy.next = head
        if not node.next:
            pre = dummy
            while cur and cur != node:
                pre = cur
                cur = cur.next
            pre.next = pre.next.next
        else:
            node.val = node.next.val
            node.next = node.next.next
        return dummy.next


import unittest


class TestSolution(unittest.TestCase):
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3

    node4 = None

    def setUp(self):
        self.s = Solution()
        self.nodes_input_to_output = [
            (self.node1, self.node2, [1, 3]),
            (self.node1, self.node1, [2, 3]),
            (self.node1, self.node3, [1, 2]),
            (self.node4, None, None),
        ]

    def test_methods(self):
        from itertools import product
        from copy import deepcopy
        for method, (node,ta, output) in product(self.s.methods(), self.nodes_input_to_output):
            test_node = deepcopy(node)
            n = getattr(self.s, method)(test_node,ta)
            if n:
                # self.assertEqual(n.output(), output)
                print(n.output(), output)
            else:
                print(n)
