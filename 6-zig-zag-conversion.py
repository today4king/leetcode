#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)



if __name__ == "__main__":
    solution = Solution()
    print('-----------')
    s = "PAYPALISHIRING"
    numRows = 3
    print(s)
    print(solution.convert(s, numRows))
    print(solution.convert(s, numRows)=='PAHNAPLSIIGYIR')
    print('-----------')
    s = "PAYPALISHIRING"
    numRows = 4
    print(s)
    print(solution.convert(s, numRows))
    print(solution.convert(s, numRows) == 'PINALSIGYAHRPI')
    print('-----------')
    s = "A"
    numRows = 1
    print(s)
    print(solution.convert(s, numRows))
    print(solution.convert(s, numRows) == 'A')
