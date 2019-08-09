#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 23:36
# @Author  : liuhu
# @Site    : 
# @File    : all_binary_Tree_Paths.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths