#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 12:09
# @Author  : liuhu
# @Site    : 
# @File    : 平衡二叉树.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.balanced = True
        def node_depth(node):
            if node is None:
                return 0
            l_depth = node_depth(node.left)+1
            r_depth = node_depth(node.right)+1
            if abs(l_depth - r_depth) >1:
                self.balanced = False
            return max(l_depth,r_depth)
        node_depth(root)
        return self.balanced