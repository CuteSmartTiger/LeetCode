#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 17:59
# @Author  : liuhu
# @Site    : 
# @File    : is_symmetric.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:                                 # 先判断根节点是否为空
            return True
        return self.isMirror(root.left, root.right)  # 分成左子树和右子树判断

    def isMirror(self, p, q):                        # 判断两棵树是否是镜像树
        if not p and not q:                          # 根节点都为空，是
            return True
        if not p or not q:                           # 其中有一棵为空，不是
            return False
        l = self.isMirror(p.left, q.right)           # p的左子树和q的右子树是否相同
        r = self.isMirror(p.right, q.left)           # p的右子树和q的左子树是否相同
        return p.val == q.val and l and r            # 值相等，并且p的左=q的右，p的右=q的左
