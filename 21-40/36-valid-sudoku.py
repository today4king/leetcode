#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import List


class Solution:
    def print_board(self, board: List[List[str]])->None:
        for row in range(9):
            r=''
            for column in range(9):
                r+= board[row][column]+'\t'
            print(r)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_bm_1 = [[0] * 9 for i in range(9)]
        board_bm_2 = [[0] * 9 for i in range(9)]
        board_bm_3 = [[0] * 9 for i in range(9)]

        for row in range(9):
            for column in range(9):
                c = board[row][column]
                if c != '.':
                    n = int(c)
                    # map bm 1
                    if board_bm_1[row][n-1] == 1:
                        return False
                    else:
                        board_bm_1[row][n-1] = 1
                    # map bm 2
                    if board_bm_2[column][n - 1] == 1:
                        return False
                    else:
                        board_bm_2[column][n - 1] = 1
                    # map bm 3
                    # sub board number
                    sb_n = row // 3 * 3 + column // 3

                    if board_bm_3[sb_n][n-1] == 1:
                        return False
                    else:
                        board_bm_3[sb_n][n-1] = 1
        return True


solution = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution.print_board(board)
print(solution.isValidSudoku(board) == True)
board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution.print_board(board)
print(solution.isValidSudoku(board) == False)
board=[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
solution.print_board(board)
print(solution.isValidSudoku(board)==False)