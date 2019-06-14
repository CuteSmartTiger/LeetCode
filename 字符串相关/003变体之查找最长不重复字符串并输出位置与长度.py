#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 12:17
# @Author  : liuhu
# @File    : 003变体之查找最长不重复字符串并输出位置与长度.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def find_max_str(s):
    tem_dic = {'str': "", "start_index": 0, "lenght": 0}
    length = len(s)
    for i in range(length):
        tmp = s[i]
        # print tmp
        for j in range(i + 1, length):
            if s[j] not in tmp:
                tmp += s[j]
            else:
                break
        if len(tmp) > tem_dic["lenght"]:
            tem_dic = {'str': tmp, "start_index": i, "lenght": len(tmp)}
    print tem_dic


find_max_str('abdfkjkgdok')
find_max_str('123daf456sdfs78fdasf042df3349')
