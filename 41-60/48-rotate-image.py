#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def swap(i, j, x, y, matrix: List[List[int]]):
            matrix[i][j] = matrix[i][j] + matrix[x][y]
            matrix[x][y] = matrix[i][j] - matrix[x][y]
            matrix[i][j] = matrix[i][j] - matrix[x][y]
            # print(matrix)

        def rotete_edge(start_r, start_c, edge_len, matrix: List[List[int]]) -> None:
            if edge_len == 1:
                return None
            l = edge_len - 1
            ml = len(matrix[0]) - 1
            for p in range(l):
                i = start_r
                j = start_c + p
                x = start_r + p
                y = start_c + l
                swap(i, j, ml - x, ml - y, matrix)
                swap(ml - x, ml - y, ml - i, ml - j, matrix)
                swap(ml - i, ml - j, x, y, matrix)

        # 四个数的坐标依次是 i,j/x,y/l-i,l-j/l-x,l-y
        matrix_len = len(matrix[0])
        r, c = 0, 0
        l = matrix_len
        while l > 0:
            rotete_edge(r, c, l, matrix)
            l -= 2
            r += 1
            c += 1


solution = Solution()
# matrix = [[1, 2], [3,4]]
# print(matrix)
# solution.rotate(matrix)
# print(matrix)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# solution.rotate(matrix)
# print(matrix)
# matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],[21,22,23,24,25]]
# print(matrix)
# solution.rotate(matrix)
# print(matrix)
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(matrix)
solution.rotate(matrix)
print(matrix)
