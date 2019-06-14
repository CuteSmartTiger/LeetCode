#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 17:26
# @Author  : liuhu
# @File    : 0071.简化路径.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def simplify_path(path):
    stack = []
    if not path.startswith(r'/'):

