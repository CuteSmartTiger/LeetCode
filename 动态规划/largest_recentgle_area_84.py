#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def largest_rectangle_area(self, heights):
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res

    def largest_rectangle_area_three(self, heights):
        stack = list()
        res, i = 0, 0
        while i < len(heights):
            if not stack or (heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                k = stack.pop()
                res = max(res, heights[k] * ((i - stack[-1] - 1) if stack else i))

        while stack:
            k = stack.pop()
            res = max(res, heights[k] * ((i - stack[-1] - 1) if stack else i))

        return res

    def largtest_recangle_area_two(self, heights):
        if not heights:
            return 0
        heights_len = len(heights)
        res = 0
        i, j = 0, 0
        while i < heights_len:
            min_h = heights[i]
            for j in range(i, heights_len):
                min_h = min(min_h, heights[j])
                res = max(res, min_h * (j - i + 1))
            i += 1

        return res

    def largest_rectangle_area_one(self, heights):
        stack = [-1]
        res = 0
        heights.append(-1)

        for idx, val in enumerate(heights):
            while heights[stack[-1]] > val:
                h = heights[stack.pop()]
                res = max(res, h * (idx - stack[-1] - 1))
            stack.append(idx)
        return res


from unittest import TestCase


class TestLargestRectangleArea(TestCase):
    def setUp(self):
        self.s = Solution()
        self.heights = [2, 1, 5, 6, 2, 3]
        self.heights_to_res = (
            ([2, 2, 2, 2, 2], 10),
            ([2], 2),
            ([1, 2, 3, 4, 5, 6, 7], 16),
            ([7, 6, 5, 4, 3, 2, 1], 16)
        )

    def test_all_functions(self):
        for heights, res in self.heights_to_res:
            self.assertEqual(self.s.largest_rectangle_area(heights), res)
