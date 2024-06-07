from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        max_left = [height[0]] +  [0] * (n-1)
        max_right = [0] * (n-1) + [height[n-1]]
        print(max_left)

        trap_value = 0
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i - 1])

        print(max_left)

        print(max_right)
        for j in range(n - 2, -1, -1):
            max_right[j] = max(max_right[j+1], height[j])
        print(max_right)

        for index, value in enumerate(height):
            trap_value += min(max_left[index], max_right[index]) - height[index]

        return trap_value

    def trapError(self, height: List[int]) -> int:
        # 错误思路，如何协助梳理正确的思路：可以多举示例，验证思路是否正确
        # left 接雨水的左侧栏
        # rigt 接雨水的右侧栏,为第一个大于等于 left 的
        # right 指针与left 直接黑色占用面积，为元素累加 temp_need_remove= 0
        # 可以接的雨水  water = (right - left +1)*min(right,left) - temp_total

        n = len(height)
        total_water = 0
        i = 0
        j = 1
        while i < n - 1 and j < n - 1:
            temp_need_remove = height[i]
            water = 0
            for j in range(i + 1, n):
                temp_need_remove += min(height[j], height[i])
                if height[j] >= height[i]:
                    water = (j - i + 1) * min(height[i], height[j]) - temp_need_remove
                    # 更新出发点
                    i = j
                    total_water += water - temp_need_remove
                    break
        return total_water


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
