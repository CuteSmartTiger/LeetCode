from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找，先确定在那一行，再确定在那一列
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        row = 0
        for i in range(n):
            if target > matrix[i][-1]:
                row = i+1

        if row > n - 1:
            return False

        cols = matrix[row]

        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if target > cols[mid]:
                left = mid + 1
            elif target < cols[mid]:
                right = mid - 1
            else:
                return True

        return False


if __name__ == '__main__':
    nums = [[1],[3]]
    target = 3
    s = Solution()
    print(s.searchMatrix(nums, target))


if __name__ == '__main__':
    logs = sys.stdin.read()
    parse_log(logs)