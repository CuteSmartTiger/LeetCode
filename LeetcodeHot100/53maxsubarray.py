from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划 dp[i] = max(dp[i-1]+ nums[i],nums[i])
        pre_sum = None
        max_sum = None
        dp = []
        for i in range(len(nums)):
            if i == 0:
                pre_sum = nums[0]
                max_sum = nums[0]
            else:
                pre_sum = max(pre_sum + nums[i], nums[i])
                if pre_sum > max_sum:
                    max_sum = pre_sum

        return max_sum if max_sum is not None else 0

    def maxSubArra1(self, nums: List[int]) -> int:
        # 动态规划 dp[i] = max(dp[i-1]+ nums[i],nums[i])
        dp = []
        for i in range(len(nums)):
            if i == 0:
                dp.append(nums[i])
            else:
                value = max(dp[i - 1] + nums[i], nums[i])
                dp.append(value)
        return max(dp) if dp else 0