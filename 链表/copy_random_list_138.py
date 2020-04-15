#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 23:52
# @Author  : liuhu
# @Site    : 
# @File    : copy_random_list.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# 第一次时的解法,None是可哈希的
# 第一步 存储对应的节点
# 存储对应的next 与random节点
def copy_random_list_1(head):
    # 遍历存储节点与复制节点的映射关系
    if not head:
        return head

    node_hash = {}
    cur = head
    while cur:
        if cur not in node_hash:
            node_hash[cur] = Node(cur.val)
            cur = cur.next
        else:
            break
    cur = head
    while cur:
        node_hash[cur].next = node_hash.get(cur.next)
        node_hash[cur].random = node_hash.get(cur.random)
        cur = cur.next

    return node_hash[head]


# BFS

# DFS
