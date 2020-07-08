#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 22:03
# @Author  : liuhu
# @Site    : 
# @File    : add_two_num.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    new_node = cur_node = ListNode(-1)
    nex = 0
    while l1 and l2:
        l1_val = l1.val
        l2_val = l2.val
        result = l1_val + l2_val + nex
        if result - 10 >= 0:
            nex = 1
            cur = result - 10
        else:
            nex = 0
            cur = result
        cur_node.next = ListNode(cur)
        cur_node = cur_node.next

        l1 = l1.next
        l2 = l2.next

    while l1:
        l1_val = l1.val
        result = l1_val + nex
        if result - 10 >= 0:
            nex = 1
            cur = result - 10
        else:
            nex = 0
            cur = result
        cur_node.next = ListNode(cur)
        cur_node = cur_node.next

        l1 = l1.next

    while l2:
        l2_val = l2.val
        result = l2_val + nex
        if result - 10 >= 0:
            nex = 1
            cur = result - 10
        else:
            nex = 0
            cur = result
        cur_node.next = ListNode(cur)
        cur_node = cur_node.next

        l2 = l2.next

    if nex:
        cur_node.next = ListNode(nex)

    return new_node.next


# 优化
def add_two_numbers(l1, l2):
    ans = ListNode(0)  # 新建一个节点，初始值为0
    temp = ans
    temp_sum = 0

    while True:
        if l1 is not None:
            temp_sum = l1.val + temp_sum  # l1链表节点值添加到总和里
            l1 = l1.next  # 指针指向下一个节点
        if l2 is not None:
            temp_sum = temp_sum + l2.val  # l2链表节点值添加到总和里
            l2 = l2.next  # 指针指向下一个节点

        temp.val = temp_sum % 10  # 取余数（满十进位），赋值当前节点值
        print(temp_sum)
        temp_sum = int(temp_sum / 10)  # 获取进位数赋值给总和（比如tempsum为10则进1位，否则进位为0），下一次节点相加，从新的总和开始。
        if l1 is None and l2 is None and temp_sum == 0:  # 直到没有进位了，同时节点位空了，跳出循环。（这里加上tempsum==0条件是因为，最后两个节
            break  # 点和值可能大于10）

        temp.next = ListNode(0)  # 新建下一个节点，存放和
        temp = temp.next  # 指针指向下一个节点

    return ans


class Solution:
    def add_two_numbers(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            nex = 0
            v = 0
            dummy = ListNode(-1)
            cur = dummy
            while l1 or l2:
                v = nex
                if l1:
                    v += l1.val
                    l1 = l1.next

                if l2:
                    v += l2.val
                    l2 = l2.next

                nex = v // 10
                v = v % 10
                cur.next = ListNode(v)
                cur = cur.next

            if nex:
                cur.next = ListNode(nex)

            return dummy.next