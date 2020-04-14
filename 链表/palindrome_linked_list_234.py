#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 23:37
# @Author  : liuhu
# @Site    : 
# @File    : palindrome_linked_list_234.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1
# 使用栈  空间复杂度O(n)
def is_palindrome_one(head):
    # 边界条件判断
    if not head or not head.next:
        return True

    stack = []
    cur = head
    while cur:
        stack.append(cur.val)
        cur = cur.next

    cur = head
    while stack:
        if cur.val != stack.pop():
            return False
        else:
            cur = cur.next

    return True

# 方法二 使用栈 O(N/2)，快慢指针
