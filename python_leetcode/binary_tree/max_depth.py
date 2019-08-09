#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 22:49
# @Author  : liuhu
# @Site    : 
# @File    : max_depth.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = []
        queue.append((1,root))
        depth = 0
        while queue:
            cur_dep, node = queue.pop(0)
            depth = max(depth, cur_dep)
            if node.left is not None:
                queue.append((cur_dep+1,node.left))
            if node.right is not None:
                queue.append((cur_dep+1,node.right))
        return depth