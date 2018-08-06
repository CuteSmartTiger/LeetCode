class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：超时
        # no_duplicate_list = []
        # for i in nums:
        #     if i not in no_duplicate_list:
        #         no_duplicate_list.append(i)
        #     else:
        #         no_duplicate_list.remove(i)
        # return no_duplicate_list.pop()

        # Approach 2: Hash Table
        # hash_table = {}
        # for i in nums:
        #     try:
        #         hash_table.pop(i)
        #     except:
        #         hash_table[i] = 1
        # return hash_table.popitem()[0]

        # Approach 3: Math
        # 2∗(a+b+c)−(a+a+b+b+c)=c
        # return 2 * sum(set(nums)) - sum(nums)

        # Approach 4: Bit Manipulation
        a = 0
        for i in nums:
            a ^= i
        return a