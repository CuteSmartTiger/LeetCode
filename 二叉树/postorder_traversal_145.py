#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 15:38
# @Author  : liuhu
# @Site    : 
# @File    : postorder_traversal_145.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 迭代  标记
    def postorder_traversal(self, root: TreeNode):
        if not root:
            return []

        post_list = []
        stack = []
        flag = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                flag.append(0)
                node = node.left
            while stack and flag[-1] == 1:
                flag.pop()
                post_list.append(stack.pop().val)

            if stack:
                flag[-1] = 1
                node = stack[-1].right
        return post_list

    # 迭代反转
    def postorder_traversal_with_reveres(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        post_list = []
        while stack:
            node = stack.pop()
            post_list.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return post_list[::-1]

    # 递归
    def postorder_traversal_recursion(self, root: TreeNode, post_list=None):
        if not root:
            return
        if post_list is None:
            post_list = []
        self.postorder_traversal_recursion(root.left, post_list)
        self.postorder_traversal_recursion(root.right, post_list)
        post_list.append(root.val)
        return post_list
