#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 12:58
# @Author  : liuhu
# @Site    : 
# @File    : inorder_traversal_94.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 使用迭代的方法(需要二刷)
def inorder_traversal_iter(root):
    if not root:
        return []
    cur = root
    stack = []
    inorder = []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        inorder.append(cur.val)
        cur = cur.right
    return inorder


# 使用递归的方法
def inorder_traversal_by_recursion(root, inorder=None):
    if not root:
        return []
    if inorder is None:
        inorder = []

    if root.left:
        inorder_traversal_by_recursion(root.left, inorder)
    inorder.append(root.val)
    if root.right:
        inorder_traversal_by_recursion(root.right, inorder)
    return inorder
