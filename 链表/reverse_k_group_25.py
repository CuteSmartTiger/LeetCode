#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 12:04
# @Author  : liuhu
# @Site    : 
# @File    : reverse_k_group_25.py
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
    def reverse_k_group(self, head, k):
        if not head or not head.next:
            return head

        cur = head
        count = 0
        while count < k and cur:
            cur = cur.next
            count += 1

        if count == k:
            node = self.reverse_k_group(cur, k)
            while count:
                # 将需要反转的这段的首节点放置到node的前面
                temp = head.next
                head.next = node

                # 更新node
                node = head
                # 更新head
                head = temp
                count -= 1
            head = node  # 这一步必须要有
        return head

    def reverse_k_group_by_tail(self, head, k):
        """尾插法"""
        dummy = ListNode(-1)
        dummy.next = head
        pre = tail = dummy  # 要理解pre与tail在初始与过程中的含义
        while True:
            count = k
            while count and tail:
                tail = tail.next
                count -= 1

            if not tail:
                break

            # 二刷时这里写错为next_pre = tail.next 这样会陷入死循环
            nex_pre = pre.next  # 这里很关键 记录下一轮的前置节点
            while pre.next != tail:
                temp = pre.next
                pre.next = temp.next

                temp.next = tail.next
                tail.next = temp

            tail = pre = nex_pre
        return dummy.next

    def reverse_k_group_with_stack(self, head, k):
        """栈"""
        if not head or not head.next:
            return head

        if k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        while head:
            cur = head
            count = 0
            stack = []
            while count < k and cur:
                stack.append(cur)
                cur = cur.next
                count += 1

            if count != k:
                pre.next = head
                break

            while stack:
                pre.next = stack.pop()
                pre = pre.next

            #  栈清空时，pre为反转后的最后一个
            # pre.next = cur 衔接下一段 这个可以省掉
            head = cur
        return dummy.next


import unittest


class TestSolution(unittest.TestCase):
    node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node2 = None

    def setUp(self):
        self.s = Solution()
        self.nodes_input_to_output = [
            (self.node1, 2, [2, 1, 4, 3, 5]),
            (self.node1, 3, [3, 2, 1, 4, 5]),
            (self.node1, 1, [1, 2, 3, 4, 5]),
            (self.node2, 3, None),
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
