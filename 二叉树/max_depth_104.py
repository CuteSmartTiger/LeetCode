#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 12:38
# @Author  : liuhu
# @Site    : 
# @File    : 二叉树的最大深度.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x, left_node=None, right_node=None):
        self.val = x
        self.left = left_node
        self.right = right_node


class Solution:

    def max_depth_queue(self, root):
        if not root:
            return 0
        from queue import Queue
        s = Queue()
        s.put((1, root))
        depth = 0
        while not s.empty():
            cur_depth, node = s.get()  # 这里一定要是先进先出，保证最后一个进入的最后出来
            depth = cur_depth  # 标记深度
            if node.left:
                s.put((cur_depth + 1, node.left))
            if node.right:
                s.put((cur_depth + 1, node.right))
        return depth

    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(1, root)]
        while queue:
            cur_depth, node = queue.pop(0)  # 这里一定要是先进先出，保证最后一个进入的最后出来
            depth = cur_depth  # 标记深度
            if node.left:
                queue.append((cur_depth + 1, node.left))
            if node.right:
                queue.append((cur_depth + 1, node.right))
        return depth

    def max_depth_recursion(self, root: TreeNode) -> int:
        if not root:
            return 0
        # return max(self.max_depth(root.left) + 1, self.max_depth(root.right) + 1)
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


import unittest


class TestRotateRight(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.binary_tree = TreeNode(
            3,
            left_node=TreeNode(9),
            right_node=TreeNode(
                20,
                left_node=TreeNode(15),
                right_node=TreeNode(7)
            )
        )

    def test_preorder_traversal_iter(self):
        depth = self.s.max_depth_queue(self.binary_tree)
        self.assertEqual(depth, 3)


