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


# 方法三 中点  反转后半部分，而不是
# 前半部分(不考虑改变原链表的前提下)
# 时间复杂度: O(N); 空间复杂度: O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        # 取中位数的上边界，比如[1, 2, 2, 3] 取到是第二个2
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 奇数时候，中点位置下一个，（这样翻转才一样）
        if fast:
            slow = slow.next
        # 翻转操作
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # 对比
        p1 = head
        p2 = prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


# 若需要判断回本并返回原链表，方法三对比后需要还原


# 递归
# copy官方题解。对于递归算法的底层实现，尤其是堆栈帧(stack frame)有详细的图解。
# 时间复杂度: O(N); 空间复杂度: O(N)，注意空间复杂度，用了栈的深度
def isPalindrome(self, head: ListNode) -> bool:
    self.front_pointer = head

    def recursively_check(current_node=head):
        if current_node is not None:
            if not recursively_check(current_node.next):
                return False
            if self.front_pointer.val != current_node.val:
                return False
            self.front_pointer = self.front_pointer.next
        return True

    return recursively_check()
