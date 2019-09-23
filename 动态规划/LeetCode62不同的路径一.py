#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 18:51
# @Author  : liuhu
# @Site    : 
# @File    : 62不同的路径一.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

def uniquePaths(m, n):
    """
    :type m: int col
    :type n: int row
    :rtype: int
    """
    martix = [[1 if j == 0 or i == 0 else 0 for i in range(m)] for j in range(n)]
    # print(martix)
    for row in range(1, n):
        for col in range(1, m):
            martix[row][col] = martix[row - 1][col] + martix[row][col - 1]
            # print(martix)
    return martix[n - 1][m - 1]


print(uniquePaths(3, 2))
print(uniquePaths(7, 3))
# m=3
# n=2
# martix = [[1 if j == 0 or i == 0 else 0 for i in range(n)] for j in range(m)]
# print(martix)

# 将上面的优化到一维数组存储
def unique_Paths( m, n):
    cur = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            cur[j] += cur[j - 1]
    return cur[-1]

