#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])

        def walk_frame(start_row, start_column, frame_width, frame_height):
            if frame_width == 1 and frame_height == 1:
                return [matrix[start_row][start_column]]
            ret = []
            if frame_width == 1:
                for i in range(frame_height):
                    ret.append(matrix[i + start_row][start_column])
                return ret
            if frame_height == 1:
                for i in range(frame_width):
                    ret.append(matrix[start_row][start_column + i])
                return ret
            # 依次顺序四个点
            # lu = start_row, start_column
            # ru = start_row, start_column+frame_width-1
            # rd = start_row + frame_height - 1, start_column+frame_width-1
            # ld = start_row + frame_height - 1, start_column
            ret = []
            for i in range(frame_width - 1):
                ret.append(matrix[start_row][start_column + i])
            for i in range(frame_height - 1):
                ret.append(matrix[start_row + i][start_column + frame_width - 1])
            for i in range(frame_width - 1):
                ret.append(matrix[start_row + frame_height - 1][start_column + frame_width - 1 - i])
            for i in range(frame_height - 1):
                ret.append(matrix[start_row + frame_height - 1 - i][start_column])
            if frame_width > 2 and frame_height > 2:
                ret += walk_frame(start_row + 1, start_column + 1, frame_width - 2, frame_height - 2)
            return ret

        return walk_frame(0, 0, width, height)


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(solution.spiralOrder(matrix))
print(solution.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5])

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matrix)
print(solution.spiralOrder(matrix))
print(solution.spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
