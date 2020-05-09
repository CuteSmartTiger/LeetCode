#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 21:51
# @Author  : liuhu
# @Site    : 
# @File    : insert_into_bst_701.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        res = []
        queue = [self]
        while queue:
            cur = queue.pop(0)
            res.append(str(cur.val)) if cur else res.append('None')
            if cur:
                queue.extend([cur.left, cur.right])
        return ','.join(res)


class Solution:
    def insert_into_bst(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return root
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return root
        return root

    def insert_into_bst_recursion(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert_into_bst_recursion(root.left, val)
        else:
            root.right = self.insert_into_bst_recursion(root.right, val)
        return root


import unittest


class TestInsertIntoBST(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.node7 = TreeNode(7)
        self.node4 = TreeNode(4)
        self.node2 = TreeNode(2)
        self.node3 = TreeNode(3, left=self.node2, right=self.node4)
        self.node6 = TreeNode(6, right=self.node7)
        self.root = TreeNode(5, left=self.node3, right=self.node6)

    def test_print(self):
        print(self.root)

    def test_insert_into_bst(self):
        node = self.s.insert_into_bst(self.root, 8)
        print(node)
