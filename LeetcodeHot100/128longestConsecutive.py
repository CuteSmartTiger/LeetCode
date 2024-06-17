from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 第一次遍历 时间复杂度 O(N),空间复杂度F(N)
        nums_set = set(nums)

        # 标记最大长度,考虑到可以是空列表
        longest = 0

        # 遍历数组，寻找连续数组的起始数
        for num in nums:
            #  找到每一个起始数，进行计算长度
            if num - 1 not in nums_set:
                cur = num
                cur_longth = 1
                while cur + 1 in nums_set:
                    cur += 1
                    cur_longth += 1
                longest = max(cur_longth, longest)

        return longest
