#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 11:28
# @Author  : liuhu
# @Site    : 
# @File    : LeetCode25k个一组反转链表(栈的方法).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 创建头部节点并与head连接
        dumy = ListNode(-1)
        dumy.next = head

        # 创建指向反转段链表的起始节点前驱与末尾的指针
        pre = dumy
        tail = dumy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            # tail 为空，则不足三个
            if not tail:
                break

            # 记录要反转的第一个节点记head，反转后其为下一段的前驱节点
            head = pre.next

            # 将这段链表的节点依次插入tail之后
            while pre.next != tail:
                # 将temp节点截取下来：
                temp = pre.next
                pre.next = temp.next

                # 将temp节点插入尾部节点之后
                temp.next = tail.next
                tail.next = temp

            # 此处的head是记录的下一段需要反转的前驱节点
            pre = head
            tail = head
        return dumy.next