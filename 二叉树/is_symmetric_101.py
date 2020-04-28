#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 23:20
# @Author  : liuhu
# @Site    : 
# @File    : 101对称二叉树.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_symmetric_iter(self, root):
        if root is None:
            return True

        queue_list = [root.left, root.right]
        while queue_list:
            left = queue_list.pop(0)
            right = queue_list.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue_list.append(left.left)
            queue_list.append(right.right)
            queue_list.append(left.right)
            queue_list.append(right.left)
        return True

    def is_symmetric_recursion(self, root):
        if root is None:
            return True
        left_node = root.left
        right_node = root.right

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            is_left_mirror = is_mirror(left.left, right.right)
            is_right_mirror = is_mirror(left.right, right.left)
            return left.val == right.val and is_left_mirror and is_right_mirror

        res = is_mirror(left_node, right_node)
        return res
