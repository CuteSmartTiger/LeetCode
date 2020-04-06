
def can_jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    step = 0
    end = 0
    max_bound = 0
    for i in range(len(nums)):
        max_bound = max(max_bound, nums[i] + i)
        if i == end and end != len(nums) - 1:
            step += 1
            end = max_bound
    return step


import unittest


class TestWays(unittest.TestCase):
    def setUp(self):
        self.nums_one = [2, 4, 1, 1, 1, 4]
        self.nums_two = [0]

    def test_num_ways(self):
        self.assertEqual(can_jump(self.nums_one), 2)
        self.assertEqual(can_jump(self.nums_two), 0)
