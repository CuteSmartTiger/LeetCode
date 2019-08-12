#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 14:46
# @Author  : liuhu
# @Site    : 
# @File    : 173_Binary_Search_Tree_Iterator.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_stack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.hasNext():
            return
        top_node = self.stack.pop()
        if top_node.right:
            self.push_stack(top_node.right)
        return top_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)

    def push_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()