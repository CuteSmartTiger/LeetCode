L=[1,3,5,4,2,1]
# print(L.index(3))
# L.reverse()
# print(L)
# for i in range(5):
#     print(L[i])

# for i in range(4,-1,-1):
#     print(L[i])

# 注意：下次尝试暴力解法

# Approach 2: Single Pass Approach
# 英文解题思路：https://leetcode.com/articles/next-permutation/

# 解题思路：
# 首先从右向左遍历数组，找到第一个相邻的左<右的数对，记右下标为x，则左下标为x - 1
# 若x > 0，则再次从右向左遍历数组，直到找到第一个大于nums[x - 1]的数字为止，记其
# 下标为y，交换nums[x - 1], nums[y]
# 最后将nums[x]及其右边的元素就地逆置


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for x in range(size - 1, -1, -1):
            if nums[x - 1] < nums[x]:
                break
        if x > 0:
            for y in range(size - 1, -1, -1):
                if nums[y] > nums[x - 1]:
                    nums[x - 1], nums[y] = nums[y], nums[x - 1]
                    break
        for z in range(int((size - x) / 2)):
            nums[x + z], nums[size - z - 1] = nums[size - z - 1], nums[x + z]
        return nums

a=Solution()
print(a.nextPermutation(L))