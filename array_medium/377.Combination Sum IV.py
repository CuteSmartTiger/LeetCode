# 377.Combination Sum IV
# 动态规划
class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] *(target+1)
        dp[0] = 1
        for x in range(target+1):
            for y in nums:
                if x+y <=target:
                    dp[x+y] += dp[x]
        return dp[target]

# dp = [0] *(7+1)
# print(dp)