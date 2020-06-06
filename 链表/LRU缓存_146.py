#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 0:08
# @Author  : liuhu
# @Site    : 
# @File    : LRU缓存_146.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import collections


class DoubleLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.nex = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        self.remove_node(self.cache[key])
        self.add_to_head(self.cache[key])
        return self.cache[key].val

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            # 移动到头部
            self.move_to_head(self.cache[key])
        else:
            # 创建新节点
            node = DoubleLinkedNode(key=key, val=value)
            # 存入cache
            self.cache[key] = node
            # 插入头部
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                remove_node = self.remove_tail()
                self.cache.pop(remove_node.key)
                self.size -= 1

    def add_to_head(self, node):
        node.nex = self.head.nex
        node.pre = self.head
        node.nex.pre = node
        self.head.nex = node

    def remove_tail(self):
        target_node = self.tail.pre
        self.remove_node(target_node)
        return target_node

    def remove_node(self, node):
        node.nex.pre = node.pre
        node.pre.nex = node.nex

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)


# 如果用继承有序字典  则实现方式为
class LRUCacheTwo(collections.OrderedDict):

    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
