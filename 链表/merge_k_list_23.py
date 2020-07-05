#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 23:28
# @Author  : liuhu
# @Site    : 
# @File    : merge_k_list_23.py
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
            if attr.startswith("__") or attr.endswith("__") or attr == 'methods'\
                    or attr.startswith('_'):
                continue
            if callable(getattr(cls, attr)):
                append(attr)
        return test_methods


class Solution(Methods):
    def merge_k_lists_with_modify(self, lists):

        def __lt__(self, other):
            return self.val < other.val

        ListNode.__lt__ = __lt__

        import heapq
        heap = []
        dummy = ListNode(-1)
        p = dummy

        for l in lists:
            if l:
                heapq.heappush(heap, l)

        while heap:
            node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next

    def merge_k_lists_with_raw_node(self, lists):
        from heapq import heappush, heappop
        nodes = []
        for index, node in enumerate(lists):
            if node:
                heappush(nodes, (node.val, index))

        dummy = ListNode(-1)
        cur = dummy
        while nodes:
            _, index = heappop(nodes)
            temp_node = lists[index]
            lists[index] = temp_node.next
            # temp_node.next = None
            cur.next = temp_node
            cur = cur.next

            if lists[index]:
                heappush(nodes, (lists[index].val, index))

        return dummy.next

    def merge_k_lists_headpq(self, lists):
        from heapq import heappush, heappop
        nodes = []
        for index, node in enumerate(lists):
            if node:
                heappush(nodes, (node.val, index))
                lists[index] = node.next

        dummy = ListNode(-1)
        cur = dummy
        while nodes:
            val, index = heappop(nodes)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[index]:
                heappush(nodes, (lists[index].val, index))
                lists[index] = lists[index].next
        return dummy.next

    def merge_k_list(self, lists):
        if not lists:
            return
        n = len(lists)
        return self.__merge(lists, 0, n - 1)

    def __merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.__merge(lists, left, mid)
        l2 = self.__merge(lists, mid + 1, right)
        return self.__merge_two_lists(l1, l2)

    def __merge_two_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.__merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.__merge_two_lists(l1, l2.next)
            return l2


import unittest


class TestSolution(unittest.TestCase):
    node1 = ListNode(1, ListNode(4, ListNode(5, )))
    node2 = ListNode(1, ListNode(3, ListNode(4, )))
    node3 = ListNode(2, ListNode(6))
    node4 = None

    def setUp(self):
        self.s = Solution()
        self.nodes_input_to_output = [(
            [self.node3, self.node2, self.node1, self.node4],
            [1, 1, 2, 3, 4, 4, 5, 6],
        )]

    def test_methods(self):
        from itertools import product
        import copy
        for method, (lists, output) in product(self.s.methods(), self.nodes_input_to_output):
            new_lists = copy.deepcopy(lists)
            n = getattr(self.s, method)(new_lists)
            if n:
                self.assertEqual(n.output(), output)
                print(n.output(), output)
            else:
                print(n)
