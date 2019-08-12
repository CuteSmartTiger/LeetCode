#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 0:54
# @Author  : liuhu
# @Site    : 
# @File    : 117_ PopulatingNextRightPointersinEachNodeII.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 利用层次遍历
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        res, cur_level = [], [root]
        while cur_level:
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(cur_level)
            cur_level = next_level

        for cur_level in res:
            for i in range(len(cur_level) - 1):
                cur_level[i].next = cur_level[i + 1]
        return root


# 迭代法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        head = None
        tail = None
        while cur:
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                        tail = cur.left
                    else:
                        tail.next = cur.left
                        tail = tail.next
                if cur.right:
                    if not head:
                        head = cur.right
                        tail = cur.right
                    else:
                        tail.next = cur.right
                        tail = tail.next
                cur = cur.next
            cur = head
            head = None
            tail = None
        return root
