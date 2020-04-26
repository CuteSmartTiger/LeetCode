#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 12:09
# @Author  : liuhu
# @Site    : 
# @File    : 平衡二叉树.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#  递归  自底向上
def is_balanced(root):
    res = [True]

    def height(node):
        if not node:
            return 0
        l_h = height(node.left) + 1
        r_h = height(node.right) + 1
        if abs(l_h - r_h) > 1:
            res[0] = False
        cur_h = max(l_h, r_h)
        return cur_h

    height(root)
    return res[0]
