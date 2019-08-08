#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 16:02
# @Author  : liuhu
# @Site    : 
# @File    : inorder.py
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res


# 非递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, res = [], []
        cur = root
        while stack or cur:
            # 将根节点及左节点压入栈中
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
