#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 12:20
# @Author  : liuhu
# @Site    : 
# @File    : delete_node_450.py
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
        return ','.join( res)


class Solution:
    def delete_node(self, root, key):
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.delete_node(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root).val
                root.right = self.delete_node(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root).val
                root.left = self.delete_node(root.left, root.val)

        return root

    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root


import unittest


class TestRotateRight(unittest.TestCase):
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

    def test_lowest_common_ancestor(self):
        node = self.s.delete_node(self.root, 7)
        print(node)
