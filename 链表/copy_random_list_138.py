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


# 复制 然后拆分 O(1)复杂度
def copy_random_list(head):
    if not head:
        return head

    # 插入复制的节点
    cur = head
    while cur:
        next_node = cur.next
        cur.next = Node(cur.val)
        cur.next.next = next_node
        cur = next_node

    # 往复制节点中关联random信息
    cur = head
    while cur:
        # 注意random指向空节点时
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    # 拆开，注意最后两的拆分，对空节点的处理
    cur = head
    copy_head = cur_copy = cur.next
    while cur_copy.next:
        cur.next = cur.next.next
        cur = cur.next

        cur_copy.next = cur_copy.next.next
        cur_copy = cur_copy.next

    cur.next = cur_copy.next
    return copy_head


class Solution:
    def copy_random_list(self, head):
        if not head:
            return head

        cur = head
        while cur:
            temp = cur.next
            cur.next = Node(cur.val, temp)
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        copy_head = copy_cur = cur.next
        while cur:
            cur.next = cur.next.next
            cur = cur.next

            if copy_cur.next:
                copy_cur.next = copy_cur.next.next
                copy_cur = copy_cur.next

        return copy_head
