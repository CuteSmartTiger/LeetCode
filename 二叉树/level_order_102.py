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
    # 解法一：利用双指针，方法三的优化，因为之前需要针对每层的节点再次遍历
    # 利用双指针，更新层级，减少遍历次数
    def level_order_two_point(self, root):
        if not root:
            return []

        from collections import deque
        q = deque()
        q.append(root)
        # last 当前行的最右节点，用来判断换行
        # nlast 下一行的最新节点
        last = root
        nlast = root
        res = []
        next_res = []
        while len(q) > 0:
            node = q.popleft()
            next_res.append(node.val)
            if node.left:
                q.append(node.left)
                nlast = node.left

            if node.right:
                q.append(node.right)
                nlast = node.right

            if node == last:
                res.append(next_res)
                last = nlast
                next_res = []
        return res

    # 解法二：递归
    def levelOrder(self, root: TreeNode, level=None, res=None):
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

    # 解法三： 迭代 列表
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

    # 解法四 双端队列
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

    # 解法五  迭代 元组,相比用栈  更好的是用队列 先进先出
    def level_order_with_q(self, root):
        if not root:
            return []
        q = [(0, root)]
        level_visited = {}
        while q:
            level, node = q.pop(0)
            if level not in level_visited:
                level_visited[level] = [node.val]
            else:
                level_visited[level].append(node.val)
            if node.left:
                q.append((level + 1, node.left))

            if node.right:
                q.append((level + 1, node.right))
        level_list = []
        for i, v in level_visited.items():
            level_list.insert(i, v)
        return level_list
