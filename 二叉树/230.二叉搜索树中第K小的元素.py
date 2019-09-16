#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 17:34
# @Author  : liuhu
# @Site    : 
# @File    : 230.二叉搜索树中第K小的元素.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest_y(self, root: TreeNode, k: int) -> int:
        result = None

        def kth(node):
            nonlocal k, result
            if node.left:
                kth(node.left)
            k -= 1
            if k == 0:
                result = node.val
                return
            if node.right:
                kth(node.right)

        kth(root)
        return result

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = None

        def helper(root):
            nonlocal k, res
            if root.left:
                helper(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            if root.right:
                helper(root.right)

        helper(root)
        return res

    def kth_smallest_iter(self, root, k):
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            k -= 1
            if k == 0:
                return tmp.val
            if tmp.right:
                cur = tmp.right