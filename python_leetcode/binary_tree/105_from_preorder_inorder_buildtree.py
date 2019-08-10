#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 23:24
# @Author  : liuhu
# @Site    : 
# @File    : 105_from_preorder_inorder_buildtree.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归 分冶 传入复制的数组
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:return None
        root = TreeNode(preorder[0])
        loc = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : loc + 1], inorder[ : loc])
        root.right = self.buildTree(preorder[loc+1 : ], inorder[loc+1: ])
        return root


# 优化内存  传入子数组边界
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        from collections import defaultdict
        n = len(preorder)
        inorder_map = defaultdict(int)
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start == pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            loc = inorder_map[preorder[pre_start]]
            # 这里要注意 因为 一开始可以明确是 pre_start + 1,in_start,loc,因为前序和中序个数是相同,所以可以求出前序左右边界
            root.left = helper(pre_start + 1, pre_start + 1 + loc - in_start, in_start, loc)
            # 根据上面用过的, 写出剩下就行了
            root.right = helper(pre_start + 1 + loc - in_start, pre_end, loc + 1, in_end)
            return root

        return helper(0, n, 0, n)
