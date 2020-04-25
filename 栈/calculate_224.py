#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 16:44
# @Author  : liuhu
# @Site    : 
# @File    : calculate_224.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Calculate:
    # 使用栈及字符串不反转，效率比反转要高
    def calculate(self, s):
        stack = []
        operand = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)

            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0

            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif ch == ')':
                res += sign * operand
                res *= stack.pop()  # stack pop 1, sign
                res += stack.pop()  # stack pop 2, operand
                # Reset the operand
                operand = 0

        return res + sign * operand

    # 栈与反转
    def calculate_reverse(self, s: str) -> int:

        stack = []  # 逆序存储
        n, operand = 0, 0  # 临时记忆连续数字字符串
        # 逆序遍历
        for v in s[::-1]:
            if v.isdigit():
                operand = 10 ** n * int(v) + operand
                n += 1
            elif v != ' ':
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                if v == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    # + ,-,)
                    stack.append(v)

        if n:
            stack.append(operand)

        return self.evaluate_expr(stack)

    def evaluate_expr(self, stack):
        res = stack.pop() if stack else 0

        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == "+":
                res += stack.pop()
            else:
                res -= stack.pop()
        return res


import unittest


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.s1 = ' ( 1+ 3) - (15+9)+123'

    def test_calculate(self):
        calculator = Calculate()
        print(calculator.calculate(self.s1))
