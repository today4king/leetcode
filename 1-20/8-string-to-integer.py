#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

from math import pow

num_letters = '1234567890'


class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        is_positive = 1
        is_dect_num = False
        int_max = int(pow(2, 31) - 1)
        pre_int_max = int_max // 10
        for c in s:
            # dect num
            if not is_dect_num:
                if c == '-':
                    is_positive = -1
                    is_dect_num = True
                elif c == '+':
                    is_dect_num = True
                elif c in num_letters:
                    is_dect_num = True
                    num = int(c)
                elif c == ' ':
                    continue
                else:
                    return 0
            elif c in num_letters:
                if is_positive>0:
                    if pre_int_max < num or (pre_int_max == num and int(c) > int_max % 10):
                        return int_max
                else:
                    if pre_int_max < num or (pre_int_max == num and int(c) > int_max % 10 + 1):
                        return int_max * is_positive-1
                num = num * 10 + int(c)
            else:
                break
        return num * is_positive


if __name__ == "__main__":
    solution = Solution()
    s = '42'
    print(solution.myAtoi(s))
    print(solution.myAtoi(s) == 42)
    print('--------------------------------')
    s = "   -42"
    print(solution.myAtoi(s))
    print(solution.myAtoi(s) == -42)
    print('--------------------------------')
    s = '4193 with words'
    print(solution.myAtoi(s))
    print(solution.myAtoi(s) == 4193)
    print('--------------------------------')
    s = 'words and 987'
    print(solution.myAtoi(s))
    print(solution.myAtoi(s) == 0)
    print('--------------------------------')
    s = "-91283472332"
    print(solution.myAtoi(s))
    print(solution.myAtoi(s) == -2147483648)
    print('--------------------------------')
