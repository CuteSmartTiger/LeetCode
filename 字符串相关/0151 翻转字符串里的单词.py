#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:11
# @Author  : liuhu
# @File    : 0151 翻转字符串里的单词.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


test = '    liu hu    ha      '
import re

res = re.split(r'\s+', test.strip())
print res.reverse()
print res



def reverse_str(test):
    res =  test.strip().split(' ',)
    temp =''
    while res:
        word = res.pop()
        if word:
           temp += ' '
           temp += word
    return temp
print reverse_str(test)


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s.strip().split(' ', )
        temp = ""
        while res:
            word = res.pop()
            if word:
                temp += " "
                temp += word

        return temp.strip()
