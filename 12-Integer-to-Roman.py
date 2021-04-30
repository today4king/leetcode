#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numbs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ret = ''
        for i, n in enumerate(numbs):
            while num >= numbs[i]:
                num -= numbs[i]
                ret += symbol[i]
        return ret


if __name__ == "__main__":
    solution = Solution()
    num = 3
    print(num)
    print(solution.intToRoman(num))
    print(solution.intToRoman(num) == "III")
    print('-------------------------------------')
    num = 4
    print(num)
    print(solution.intToRoman(num))
    print(solution.intToRoman(num) == "IV")
    print('-------------------------------------')
    num = 9
    print(num)
    print(solution.intToRoman(num))
    print(solution.intToRoman(num) == "IX")
    print('-------------------------------------')
    num = 58
    print(num)
    print(solution.intToRoman(num))
    print(solution.intToRoman(num) == "LVIII")
    print('-------------------------------------')
    num = 1994
    print(num)
    print(solution.intToRoman(num))
    print(solution.intToRoman(num) == "MCMXCIV")
    print('-------------------------------------')
