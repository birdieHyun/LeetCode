from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_idx = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_idx.append((j, i))

        if zero_idx:
            for i in zero_idx:
                x, y = i
                matrix[y] = [0] * len(matrix[0])

                for j in range(len(matrix)):
                    matrix[j][x] = 0

        print(matrix)