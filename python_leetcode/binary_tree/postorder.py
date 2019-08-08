#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 14:57
# @Author  : liuhu
# @Site    : 
# @File    : postorder.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 非递归迭代方法，类似于层次遍历
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        return output[::-1]

# 递归的方法
class Solution:
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res