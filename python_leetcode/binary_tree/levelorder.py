#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 17:16
# @Author  : liuhu
# @Site    : 
# @File    : levelorder.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        cur_level = [root]
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp)
            cur_level = next_level
        return res
