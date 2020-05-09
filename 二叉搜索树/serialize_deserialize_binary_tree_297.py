#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 0:17
# @Author  : liuhu
# @Site    : 
# @File    : serialize_deserialize_binary_tree_297.py
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


# 递归的方法
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def rser(node, s=''):
            if not node:
                s += 'N,'
            else:
                s += '{},'.format(node.val)
                s = rser(node.left, s)
                s = rser(node.right, s)
            return s

        return rser(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdes(node_list):
            if node_list[0] == 'N':
                node_list.pop(0)
                return None
            root = TreeNode(int(node_list.pop(0)))
            root.left = rdes(node_list)
            root.right = rdes(node_list)
            return root

        node_list = data.split(',')
        return rdes(node_list)


import unittest


class TestDeleteNode(unittest.TestCase):
    def setUp(self):
        self.s = Codec()
        self.node7 = TreeNode(7)
        self.node4 = TreeNode(4)
        self.node2 = TreeNode(2)
        self.node3 = TreeNode(3, left=self.node2, right=self.node4)
        self.node6 = TreeNode(6, right=self.node7)
        self.root = TreeNode(5, left=self.node3, right=self.node6)

    def test_ser_node(self):
        print(self.root)
        s = self.s.serialize(self.root)
        print(s)
        node = self.s.deserialize(s)
        print(node)
