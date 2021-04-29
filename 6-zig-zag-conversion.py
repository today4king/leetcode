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
    def get_coordinate(self, i, numRows):
        m = numRows * 2 - 2
        mod = i % m
        x = 0
        if mod > numRows:
            x = mod - numRows

            y = numRows -x

            x += int(i / m) * (numRows - 1)+1
        elif mod==0:
            y = 2
            x += int(i / m) * (numRows - 1)
        else:
            y = mod
            x += int(i / m) * (numRows - 1) + 1

        return x - 1, y - 1

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        m = numRows * 2 - 2
        sl = len(s)
        columnNum = sl % m % numRows + 1 + int(sl / m) * (numRows - 1)
        matrix = [[''] * columnNum for i in range(numRows)]

        for i, c in enumerate(s):
            x, y = self.get_coordinate(i + 1, numRows)
            #print('%d,%d'%(x,y))
            matrix[y][x] = c
        ret = ''

        for y in range(numRows):
            # line=''
            for x in range(columnNum):
                ret += matrix[y][x]
                # if matrix[y][x]=='':
                #     line+=' '
                # else:
                #     line += matrix[y][x]
            #print(line)
        return ret


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
