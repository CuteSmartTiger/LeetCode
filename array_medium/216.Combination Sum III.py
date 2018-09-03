# 216.Combination Sum III
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        Solution.re = []
        self.backtracking(k, n, 1, [])
        return Solution.re

    def backtracking(self, k, n, start, val):
        if k == 0 and n == 0:
            Solution.re.append(val)
        else:
            for i in range(start, 10):
                if n < i:
                    break
                self.backtracking(k - 1, n - i, i + 1, val + [i])

