#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 22:48
# @Author  : liuhu
# @Site    : 
# @File    : 106_inorder_postorder_buildtree.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 分治法  递归
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        assert len(inorder) == len(postorder)

        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            # 这里要返回结点，而不是返回具体的数
            # assert inorder[0] == postorder[0]
            return TreeNode(inorder[0])
        # 后序遍历的最后一个结点就是根结点
        root = TreeNode(postorder[-1])
        # 在中序遍历中找到根结点的索引，得到左右子树的一个划分
        pos = inorder.index(postorder[-1])
        # 这里的列表切片使用的是复制值，使用了一些空间，因此空间复杂度是 O(N)
        root.left = self.buildTree(inorder[:pos], postorder[:pos])
        root.right = self.buildTree(inorder[pos + 1:], postorder[pos:-1])
        return root