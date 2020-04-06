# 1. 设置cur_reach_max_index 为当前可达的最远位置,当前位置及之前的位置中所能够到达的最远；
# 2. cur_i_reach_max__index 为遍历各个位置i过程中，各个位置i能达到的最远位置；
# 3. less_jump为最少跳跃次数
# 4. 利用i遍历nums数组，如i超过cur_reach_max_index，则less_jump加1,cur_reach_max_index = cur_i_reach_max__index，
# 遍历过程中，如果cur_i_reach_max__index < nums[i] + i 则更新cur_i_reach_max__index
# 5. 当cur_reach_max_index大于或等于最大索引时，则返回最少次数
def jump(nums):
    length = len(nums)
    if length < 2:
        return 0
    cur_reach_max_index = nums[0]
    cur_i_reach_max__index = nums[0]
    less_jump = 1
    for i in range(length):
        if cur_reach_max_index < i:
            cur_reach_max_index =cur_i_reach_max__index
            res += 1
        if cur_i_reach_max__index < nums[i] + i:
            cur_i_reach_max__index =  nums[i] + i
    return less_jump
