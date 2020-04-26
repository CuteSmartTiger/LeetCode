#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 19:50
# @Author  : liuhu
# @Site    : 
# @File    : level_order_102.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def levelOrder(self, root: TreeNode, level=None, res=None) -> List[List[int]]:
        if not root:
            return []
        if level is None:
            level = 0
        if res is None:
            res = []
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        self.levelOrder(root.left, level=level + 1, res=res)
        self.levelOrder(root.right, level=level + 1, res=res)
        return res

    #  迭代 列表
    def level_order_iter(self, root):
        if not root:
            return []
        cur_level = [root]
        res = []
        while cur_level:
            cur_res = []
            next_level = []
            for node in cur_level:
                cur_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(cur_res)
            cur_level = next_level
        return res

    # 双端队列
    def level_order_deque(self, root):
        from collections import deque
        if not root:
            return []
        d = deque()
        d.append((0, root))
        level_visited = {}
        while d:
            level, node = d.popleft()
            if level not in level_visited:
                level_visited[level] = [node.val]
            else:
                level_visited[level].append(node.val)
            if node.left:
                d.append((level + 1, node.left))

            if node.right:
                d.append((level + 1, node.right))
        level_list = []
        for i, v in level_visited.items():
            level_list.insert(i, v)
        return level_list

    # 迭代 元组
    def level_order_with_stack(self, root):
        if not root:
            return []
        stack = [(0, root)]
        level_visited = {}
        while stack:
            level, node = stack[0]
            if level not in level_visited:
                level_visited[level] = [node.val]
            else:
                level_visited[level].append(node.val)
            if node.left:
                stack.append((level + 1, node.left))

            if node.right:
                stack.append((level + 1, node.right))
            stack = stack[1:]
        level_list = []
        for i, v in level_visited.items():
            level_list.insert(i, v)
        return level_list
