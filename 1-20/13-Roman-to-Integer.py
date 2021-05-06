#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numbs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ret = 0
        j = 0
        for i, n in enumerate(symbol):
            while j < len(s):
                if symbol[i] in s[j::] and symbol[i][0] == s[j]:
                    ret += numbs[i]
                    j += len(symbol[i])
                else:
                    break
        return ret


if __name__ == "__main__":
    solution = Solution()
    num = 'III'
    print(num)
    print(solution.romanToInt(num))
    print(solution.romanToInt(num) == 3)
    print('-------------------------------------')
    num = 'IV'
    print(num)
    print(solution.romanToInt(num))
    print(solution.romanToInt(num) == 4)
    print('-------------------------------------')
    num = "IX"
    print(num)
    print(solution.romanToInt(num))
    print(solution.romanToInt(num) == 9)
    print('-------------------------------------')
    num = "LVIII"
    print(num)
    print(solution.romanToInt(num))
    print(solution.romanToInt(num) == 58)
    print('-------------------------------------')
    num = "MCMXCIV"
    print(num)
    print(solution.romanToInt(num))
    print(solution.romanToInt(num) == 1994)
    print('-------------------------------------')
