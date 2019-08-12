#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 12:29
# @Author  : liuhu
# @Site    : 
# @File    : 98_Validate_Binary_Search_Tree.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 利用中序遍历有序    递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        res = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False
        return True
        # return res==sorted(res) and len(res) == len(set(res))


