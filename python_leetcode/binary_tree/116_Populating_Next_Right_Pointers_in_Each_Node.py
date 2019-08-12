#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 0:36
# @Author  : liuhu
# @Site    : 
# @File    : 116_Populating_Next_Right_Pointers_in_Each_Node.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 队列
def connect(self, root: 'Node') -> 'Node':
    from collections import deque
    if not root: return root
    queue = deque()
    queue.appendleft(root)
    while queue:
        p = None
        n = len(queue)
        for _ in range(n):
            tmp = queue.pop()
            if p:
                p.next = tmp
                p = p.next
            else:
                p = tmp
            if tmp.left:
                queue.appendleft(tmp.left)
            if tmp.right:
                queue.appendleft(tmp.right)
        p.next = None
    return root

#  递归
def connect1(self, root: 'Node') -> 'Node':
    if not root:
        return
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
    self.connect(root.left)
    self.connect(root.right)
    return root


# 迭代拉链
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pre = root
        while pre:
            cur = pre
            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.right and cur.next: cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root

