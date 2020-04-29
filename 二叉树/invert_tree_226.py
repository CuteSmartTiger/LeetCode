#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 22:49
# @Author  : liuhu
# @Site    : 
# @File    : invert_tree_226.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


#  不论递归还是迭代的思路 其本质为：
# 交换节点的左右节点
def invert_tree_by_iter(root):
    if not root:
        return root

    from collections import deque
    q = deque()
    q.append(root)
    while len(q):
        node = q.popleft()
        node.right, node.left = node.left, node.right
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return root


def invert_tree(self, root):
    if not root:
        return root

    root.left, root.right = root.right, root.left
    root.left = self.invertTree(root.left)
    root.right = self.invertTree(root.right)
    return root
