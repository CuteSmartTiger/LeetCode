# 33.Search in Rotated Sorted Array 
# （1）如果target==A[m]，那么m就是我们要的结果，直接返回；
# （2）如果A[m]<A[r]，那么说明从m到r一定是有序的（没有受到rotate的影响），
# 那么我们只需要判断target是不是在m到r之间，如果是则把左边缘移到m+1，否则
# 就target在另一半，即把右边缘移到m-1。
# （3）如果A[m]>=A[r]，那么说明从l到m一定是有序的，同样只需要判断target是
# 否在这个范围内，相应的移动边缘即可。根据以上方法，每次我们都可以切掉一半的
# 数据，所以算法的时间复杂度是O(logn)，空间复杂度是O(1)
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 标记每次查询的左右
        L = 0
        R = len(nums)-1
        while L <= R:
            m = (R+L)//2
            if target == nums[m]:
                return m
            if nums[m] < nums[R]:
                if target > nums[m] and target <= nums[R]:
                    L = m+1
                else:
                    R = m-1
            else:
                if target >= nums[L] and target < nums[m]:
                    R = m-1
                else:
                    L = m+1
        return -1