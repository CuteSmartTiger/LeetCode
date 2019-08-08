#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 16:02
# @Author  : liuhu
# @Site    : 
# @File    : preorder.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res

# 非递归 栈
class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return res
