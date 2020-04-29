#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 23:23
# @Author  : liuhu
# @Site    : 
# @File    : lowest_common_ancestor_236.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class TreeNode:
    def __init__(self, x, left_node=None, right_node=None):
        self.val = x
        self.left = left_node
        self.right = right_node


class Solution:
    def lowest_common_ancestor(self, root, p, q):
        # 定义由子节点获取父节点的字典
        parent = {root: None}

        stack = [root]
        # 寻找直到p q 的父节点找到
        while p not in parent or q not in parent:
            ndoe = stack.pop()
            if ndoe.left:
                parent[ndoe.left] = ndoe
                stack.append(ndoe.left)

            if ndoe.right:
                parent[ndoe.right] = ndoe
                stack.append(ndoe.right)

        visited = set()
        # 存储p节点到根节点的线路上的节点
        while p:
            visited.add(p)  # 注意 第一次的时候这里写成了parent[p],导致出错
            p = parent[p]
        # 从q往父节点寻找首次出现在visited总的节点
        while q not in visited:
            q = parent[q]

        return q


import unittest


class TestRotateRight(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.node7 = TreeNode(7)
        self.node4 = TreeNode(4)
        self.node2 = TreeNode(2, left_node=self.node7, right_node=self.node4)
        self.node6 = TreeNode(6)
        self.node5 = TreeNode(5, left_node=self.node6, right_node=self.node2)
        self.node0 = TreeNode(0)
        self.node8 = TreeNode(8)
        self.node1 = TreeNode(1, left_node=self.node0, right_node=self.node8)
        self.root = TreeNode(3, left_node=self.node5, right_node=self.node1)

    def test_lowest_common_ancestor(self):
        node = self.s.lowest_common_ancestor(self.root, self.node5, self.node1)
        self.assertEqual(node, self.root)

        node = self.s.lowest_common_ancestor(self.root, self.node5, self.node4)
        self.assertEqual(node, self.node5)
