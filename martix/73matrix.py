from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited_raw_zero = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    visited_raw_zero.append([i, j])

        for raw in visited_raw_zero:
            i, j = raw[0], raw[1]

            for a in range(n):
                matrix[a][j] = 0

            for b in range(m):
                matrix[i][b] = 0

        return matrix

if __name__ == '__main__':
    s =Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    print(s.setZeroes(matrix))
