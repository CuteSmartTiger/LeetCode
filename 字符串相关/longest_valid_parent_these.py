#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 11:19
# @Author  : liuhu
# @Site    : 
# @File    : longest_valid_parent_these.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 与找到每个可能的子字符串后再判断它的有效性不同，
# 我们可以用栈在遍历给定字符串的过程中去判断到
# 目前为止扫描的子字符串的有效性，同时计算最
# 长有效字符串的长度。我们首先将 -1 放入栈顶，
# 之所以放入-1，可以现象()中情况索引情况，( pop出来后栈为空
# 对于遇到的每个 ‘(‘ ，我们将它的下标放入栈中。
# 对于遇到的每个 ‘)’ ，我们弹出栈顶的元素并将
# 当前元素的下标与此时栈顶值作差，得出当前有效括
# 号字符串的长度。并最终返回最长有效子字符串的长度

# 时间复杂度： O(n) ， nn 是给定字符串的长度。
# 空间复杂度： O(n)， 栈的大小最大达到 nn


def longest_valid_parentheses(s):
    max_length = 0
    stack = [-1]
    for index, value in enumerate(s):
        if value == '(':
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                # 当栈中为空时即没有左括号的索引，
                # value为多余的右括号，此时将其索引
                # 加入栈中，此时计算的长度为0
                stack.append(index)
            i = stack[-1]
            max_length = max(max_length, index - i)
    return max_length


# 时间复杂度： O(n),遍历两遍字符串。
# 空间复杂度： O(1),仅有两个额外的变量 left 和 right
def longest_valid_parentheses_by_left_and_right(s):
    left = right = 0
    n = len(s)
    max_length = 0
    for i in range(n):
        if s[i] == "(":
            left += 1
        else:
            right += 1
        if right > left:
            left = right = 0
        elif right == left:
            max_length = max(max_length, 2 * left)
        else:
            pass

    left = right = 0
    for v in s[::-1]:
        if v == "(":
            left += 1
        else:
            right += 1
        if right < left:
            left = right = 0
        elif right == left:
            max_length = max(max_length, 2 * left)
        else:
            pass
    return max_length


# 方法三使用动态规划
def longest_valid_parentheses_with_dp(s):
    n = len(s)
    dp = [0 for i in range(n)]
    max_length = 0
    for i in range(1, n):
        if s[i] == ")":
            if s[i - 1] == '(':
                if i == 1:
                    dp[i] = 2
                else:
                    dp[i] = dp[i - 2] + 2
            else:
                if s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

            max_length = max(max_length, dp[i])
    return max_length
