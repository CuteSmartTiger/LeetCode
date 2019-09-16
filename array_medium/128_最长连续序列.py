# 判断每一个数字的前一个与后续序列是否存在表中
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 集合的查找复杂度为O(1)
        nums = set(nums)
        res = 0
        for num in nums:
            # 判断x是否是可组成连续数组的第一个数字，
            # 因为x若为连续序列的非第一数字，则x-1必存在nums中
            # 这个判断很重要，可以将重复序列的计算去重
            if num-1 not in nums:
                next_num = num + 1
                #判断下一个数字是否存在集合中，存在则继续迭代
                while next_num in nums:
                    next_num += 1
                # 更新最大长度
                res = max(res,next_num-num)
        return res

# 用字典
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 记录首尾值的最长长度
        lookup = {}
        res = 0
        for num in nums:
            if num not in lookup:
                # 判断左右是否可以连起来
                left = lookup[num - 1] if num - 1 in lookup else 0
                right = lookup[num + 1] if num + 1 in lookup else 0
                # 记录长度
                lookup[num] = left + right + 1
                # 把头尾都设置为最长长度
                lookup[num - left] = left + right + 1
                lookup[num + right] = left + right + 1
                res = max(res, left + right + 1)
        return res
