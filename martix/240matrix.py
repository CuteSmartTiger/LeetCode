from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 先找可能所在的列
        if not matrix or not matrix[0]:
            return False

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[0][mid]:
                left = mid + 1
            elif target < matrix[0][mid]:
                right = mid - 1
            else:
                return True

        col = left - 1
        if col <0 or col > len(matrix[0]) - 1:
            return False

        t,d = 0,len(matrix)-1

        while t <= d:
            mid = (t + d )//2
            if target > matrix[mid][col]:
                t = mid +1
            elif target < matrix[mid][col]:
                d = mid -1
            else:
                return True
        return False
if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 19
    s = Solution()
    print(s.searchMatrix(matrix, target))