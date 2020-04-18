#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 17:57
# @Author  : liuhu
# @Site    : 
# @File    : has_cycle_and_return_enter.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# hash
def detect_cycle_by_set(head):
    save_set = {None}
    while head:
        if head not in save_set:
            save_set.add(head)
            head = head.next
        else:
            return head
    return None


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
