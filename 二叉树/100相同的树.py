#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 23:38
# @Author  : liuhu
# @Site    : 
# @File    : 100相同的树.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        node_queue = [p, q]
        while node_queue:
            lf = node_queue.pop(0)
            rf = node_queue.pop(0)
            if not lf and not rf:
                continue
            if not lf or not rf:
                return False
            if lf.val != rf.val:
                return False
            node_queue.append(lf.left)
            node_queue.append(rf.left)
            node_queue.append(lf.right)
            node_queue.append(rf.right)
        return True

    def is_same_tree_iter(self, p, q):
        node_queue = [p, q]
        while node_queue:
            lf = node_queue.pop(0)
            rf = node_queue.pop(0)
            if not lf and not rf:
                continue
            if not lf or not rf:
                return False
            if lf.val != rf.val:
                return False
            node_queue.append(lf.left)
            node_queue.append(rf.left)
            node_queue.append(lf.right)
            node_queue.append(rf.right)
        return True

    def is_same_tree_recursion(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        res_l = self.isSameTree(p.left, q.left)
        res_r = self.isSameTree(p.right, q.right)
        return res_l and res_r

