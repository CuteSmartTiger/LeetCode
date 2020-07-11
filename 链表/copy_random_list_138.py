#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 23:52
# @Author  : liuhu
# @Site    : 
# @File    : copy_random_list.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def output(self):
        visited = {}
        output = []
        append = output.append
        cur = self
        while cur:
            if cur not in visited:
                append((cur.val, cur.random.val if cur.random is not None else None))
                cur = cur.next
            else:
                break
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

    def copy_random_list_by_hash(self, head):
        # 遍历存储节点与复制节点的映射关系
        if not head:
            return head

        node_hash = {}
        cur = head
        while cur:
            if cur not in node_hash:
                node_hash[cur] = Node(cur.val)
                cur = cur.next
            else:
                break
        cur = head
        while cur:
            node_hash[cur].next = node_hash.get(cur.next)
            node_hash[cur].random = node_hash.get(cur.random)
            cur = cur.next

        return node_hash[head]

    def copy_random_list(self, head):
        if not head:
            return head

        cur = head
        while cur:
            temp = cur.next
            cur.next = Node(cur.val, temp)
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        copy_head = copy_cur = cur.next
        while cur:
            cur.next = cur.next.next
            cur = cur.next

            if copy_cur.next:
                copy_cur.next = copy_cur.next.next
                copy_cur = copy_cur.next

        return copy_head


import unittest


class TestSolution(unittest.TestCase):
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node1.random = node3
    node2.random = node2

    node4 = None

    node5 = Node(1)
    node5.next = node5
    # node5.random = node5

    def setUp(self):
        self.s = Solution()
        self.nodes_input_to_output = [
            (self.node1, [(1, 3), (2, 2), (3, None)]),
            (self.node4, Node),
            # (self.node5, [(1, 1)]),
            (self.node5, [(1, 1)]),
        ]

    def test_methods(self):
        from itertools import product
        from copy import deepcopy
        for method, (node, output) in product(self.s.methods(), self.nodes_input_to_output):
            test_node = deepcopy(node)
            n = getattr(self.s, method)(test_node)
            if n:
                self.assertEqual(n.output(), output)
                print(n.output(), output)
            else:
                print(n)
