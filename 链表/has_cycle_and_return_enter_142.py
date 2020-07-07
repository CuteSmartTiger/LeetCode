#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 17:57
# @Author  : liuhu
# @Site    : 
# @File    : has_cycle_and_return_enter.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Solution:
    def detect_cycle(self, head):
        if not head:
            return

        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return
        else:
            cur = head
            while cur != slow:
                cur = cur.next
                slow = slow.next
            return cur


def detect_cycle(head):
    if not head:
        return None

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            # 假设slow走过n个节点在环内M点相遇，则fast走了2n节点
            # 则此时other指针起始点开始一次走一步,show也一次走一步，
            # 当other走了n步时，一定到达M点，而此时slow走了2n步，也
            # 到达M点，则相遇，这次other与slow在M点相遇，考虑他们每次
            # 移动一个指针，则其一定在入口点相遇，故需求第一个相遇点
            other = head
            while other != slow:
                other = other.next
                slow = slow.next
            return other
    return False
