#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 14:15
# @Author  : liuhu
# @Site    : 
# @File    : preorder_traversal_144.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class TreeNode:
    def __init__(self, x, left_node=None, right_node=None):
        self.val = x
        self.left = left_node
        self.right = right_node


class Solution:
    def preorder_traversal_iter(self, root):
        if not root:
            return []
        pre_list = []
        stack = [root]
        while stack:
            root = stack.pop()
            pre_list.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return pre_list

    def preorder_traversal_recursion(self, root, pre_list=None):
        if not root:
            return []

        if pre_list is None:
            pre_list = []

        pre_list.append(root.val)
        self.preorder_traversal_recursion(root.left, pre_list)
        self.preorder_traversal_recursion(root.right, pre_list)
        return pre_list


import unittest


class TestRotateRight(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.binary_tree = TreeNode(
            1,
            left_node=TreeNode(-1),
            right_node=TreeNode(
                2,
                left_node=TreeNode(3),
                right_node=TreeNode(4)
            )
        )

    def test_preorder_traversal_iter(self):
        pre_order = self.s.preorder_traversal_iter(self.binary_tree)
        self.assertEqual(pre_order,[1, -1, 2, 3, 4])

    def test_preorder_traversal_recursion(self):
        pre_order = self.s.preorder_traversal_recursion(self.binary_tree)
        self.assertEqual(pre_order, [1, -1, 2, 3, 4])

