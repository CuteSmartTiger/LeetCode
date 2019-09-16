#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 12:38
# @Author  : liuhu
# @Site    : 
# @File    : 二叉树的最大深度.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

    def max_depth_recursion(self, root):
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

    def max_depth_iter(self, root):
        if root is None:
            return 0
        queue = []
        queue.append((1, root))
        depth = 0
        while queue:
            cur_dep, node = queue.pop(0)
            # depth = max(depth, cur_dep)
            depth = cur_dep
            if node.left is not None:
                queue.append((cur_dep + 1, node.left))
            if node.right is not None:
                queue.append((cur_dep + 1, node.right))
        return depth