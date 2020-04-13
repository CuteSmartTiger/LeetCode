#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 23:26
# @Author  : liuhu
# @Site    : 
# @File    : rotate_right_61.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotate_right_error(head, k):
    """error"""
    # 空链表再怎么移动也是空
    if not head or not head.next:
        return head

    # 快慢指针，然后左截断，右指向头部
    pre_head = ListNode(0)
    pre_head.next = head

    # 获取链表的长度
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    left = right = pre_head
    # 取模
    move_k = k % n
    while move_k:
        right = right.next
        move_k = -1

    while right and right.next:
        left = left.next
        right = right.next

    # 新链表头部
    new_head = left.next
    # 截断
    left.next = right.next
    # 指向旧头部
    right.next = pre_head.next

    return new_head


# 1.遍历第一遍，求出链表长度，并获得最后一个节点。
# 2.将链表首尾相接。
# 3.题目中头结点是向前挪k%len次，但程序中只能往后挪，所以将头节点向后挪 len - (k%len) 次。
# 4.断开链表，取回结果
def rotate_right(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not (head and head.next):
        return head
    first = head
    len_list = 1
    while head.next:
        len_list += 1
        head = head.next
    head.next = first
    for i in range(len_list - k % len_list):
        head = head.next
    result = head.next
    head.next = None
    return result
