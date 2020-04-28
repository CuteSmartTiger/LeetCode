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


class Solution:
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
