#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 14:41
# @Author  : liuhu
# @Site    : 
# @File    : has_cycle_141.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 使用快慢指针
def has_cycle(head) -> bool:
    # 快慢指针
    if not head:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


