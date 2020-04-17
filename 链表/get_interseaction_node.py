#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 0:01
# @Author  : liuhu
# @Site    : 
# @File    : get_interseaction_node.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# - 160. 相交链表:编写一个程序，找到两个单链表相交的起始节点。
# - 思路：表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。则当两链表走到相等的位置时：
# x1+y+x2 = x2+y+x1
def get_intersection_node(headA, headB):
    a = headA
    b = headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
        # 如果不想交，则第二遍时最终a b 为空指针时跳出循环
    return a


def get_intersection_node_method_one(headA, headB):
    if not headA or not headB:
        return None
    cur = headA
    na = 1
    while cur.next:
        na += 1

    cur = headB
    nb = 1
    while cur.next:
        nb += 1
    k = na - nb
    cura = headA
    curb = headB
    if k == 0:
        pass
    elif k > 0:
        while k > 0:
            cura = cura.next
            k -= 1
    else:
        while k < 0:
            curb = curb.next
            k += 1
    while cura != curb:
        cura = cura.next
        curb = curb.next
    return cura
