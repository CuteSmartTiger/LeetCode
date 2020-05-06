#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 15:49
# @Author  : liuhu
# @Site    : 
# @File    : 验证二叉搜索树.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None

        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            return isBST(root.right)

        return isBST(root)

    def is_ValidBST_iter(self, root: TreeNode) -> bool:
        stack = []
        p = root
        pre = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if pre and p.val <= pre.val:
                return False
            pre = p
            p = p.right
        return True

    def is_valid_bst_in_order(self, root):
        res = []

        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            res.append(node.val)
            in_order(node.right)

        in_order(root)
        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False
        return True

    def is_valid_bst_by_recursion_one(self, root):
        def in_order(node, res=None):
            if not node:
                return
            if res is None:
                res = []
            in_order(node.left, res=res)
            res.append(node.val)
            in_order(node.right, res=res)

        ret = []
        in_order(root, res=ret)
        if sorted(ret) == ret and len(set(ret)) == len(ret):
            return True
        else:
            return False
