#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 12:58
# @Author  : liuhu
# @Site    : 
# @File    : inorder_traversal_94.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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

    def inorder_tra(self, root):
        if not root:
            return []
        pre_visited = []
        stack = [root]
        while stack:
            node = stack[-1]
            stack.pop()
            if node is not None:
                if node.right:
                    stack.append(node.right)

                stack.append(node)
                stack.append(None)

                if node.left:
                    stack.append(node.left)

            else:
                pre_visited.append(stack.pop().val)

        return pre_visited


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
