#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 10:55
# @Author  : liuhu
# @File    : 003查找字符串中最大不重复的子串.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# def lengthOfLongestSubstring( s):
#     res = 0
#     left = 0
#     d = {}
#
#     for i, ch in enumerate(s):
#         print i,ch
#         if ch in d and d[ch] >= left:
#             left = d[ch] + 1
#         d[ch] = i
#         res = max(res, i - left + 1)
#     return res
#
#
# # one_str_list = ['120135435', 'abdfkjkgdok', '123456780423349']
# one_str_list = ['abdfkjkgdok']
# for one_str in one_str_list:
#     res = lengthOfLongestSubstring(one_str)
#     print '{0}最长非重复子串为：{1}'.format(one_str, res)


def find_longest_no_repeat_substr(one_str):
    '''''
    找出来一个字符串中最长不重复子串
    '''
    res_list = []
    length = len(one_str)
    for i in range(length):
        tmp = one_str[i]
        for j in range(i + 1, length):
            if one_str[j] not in tmp:
                tmp += one_str[j]
            else:
                break
        res_list.append(tmp)
    res_list.sort(lambda x, y: cmp(len(x), len(y)))
    return res_list[-1]


if __name__ == '__main__':
    one_str_list = ['120135435', 'abdfkjkgdok', '123456780423349']
    for one_str in one_str_list:
        res = find_longest_no_repeat_substr(one_str)
        print '{0}最长非重复子串为：{1}'.format(one_str, res)
