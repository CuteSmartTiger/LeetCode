# 80.Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        L = len(nums)
        dup = 0
        tmp = nums[0]
        for i in range(1,L):
            if nums[i] == tmp:
                dup += 1
            else:
                dup = 0
                tmp = nums[i]
            if dup >= 2:
                nums[i] = '#'

        for i in range(L-1, -1, -1):
            if nums[i] == '#':
                nums.pop(i)
        return len(nums)