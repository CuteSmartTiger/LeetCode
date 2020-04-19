#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 12:04
# @Author  : liuhu
# @Site    : 
# @File    : reverse_k_group_25.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def output(self):
        print_list = []
        cur = self
        while cur:
            print_list.append(cur.val)
            cur = cur.next
        return print_list


# 尾插法
def reverse_k_group(head, k):
    if not isinstance(k, int) or k < 1:
        raise ValueError('k must be int  and >=1')

    pre_head = ListNode(0)
    pre_head.next = head
    pre = tail = pre_head
    while True:
        # 前置节点pre指针与tail尾指针
        count = k
        while count and tail:
            tail = tail.next
            count -= 1
        if not tail:
            break

        head = pre.next
        while pre.next != tail:
            # 将temp节点截取下来
            temp = pre.next
            pre.next = temp.next

            # 将截取下的节点放入到尾节点之后
            temp.next = tail.next
            tail.next = temp

        pre = head
        tail = head

    return pre_head.next


import unittest


class TestRotateRight(unittest.TestCase):
    node5 = ListNode(5)
    node4 = ListNode(4)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    k = 2

    def setUp(self):
        pass

    @staticmethod
    def _get_node_deepcopy(target_node):
        import copy
        return copy.deepcopy(target_node)

    def test_reverse_k_one(self):
        rotate_link = reverse_k_group(self._get_node_deepcopy(self.node1), 2)
        self.assertEqual(rotate_link.output(), [2, 1, 4, 3, 5])
        print(self.node1.output())

    def test_reverse_k_two(self):
        rotate_link = reverse_k_group(self._get_node_deepcopy(self.node1), 5)
        self.assertEqual(rotate_link.output(), [5, 4, 3, 2, 1])

        rotate_link = reverse_k_group(self._get_node_deepcopy(self.node1), 6)
        self.assertEqual(rotate_link.output(), [1, 2, 3, 4, 5])

        rotate_link = reverse_k_group(self._get_node_deepcopy(self.node1), 1)
        self.assertEqual(rotate_link.output(), [1, 2, 3, 4, 5])

        rotate_link = reverse_k_group(self._get_node_deepcopy(self.node1), 0)
        self.assertEqual(rotate_link.output(), [1, 2, 3, 4, 5])
