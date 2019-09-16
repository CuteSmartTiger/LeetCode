#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 17:59
# @Author  : liuhu
# @Site    : 
# @File    : 不用乘除法及判断关键字求和.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
from functools import reduce
res_list = range(1, 20000)
sum_result = reduce(lambda x, y: x + y, res_list)
print(sum_result)
