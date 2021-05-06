#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
from math import pow


class Solution:
    def reverse(self, x: int) -> int:
        int_max = int(pow(2, 31)) - 1

        ret = 0
        flag = -1 if x < 0 else 1
        x = x * flag
        if x < 10:
            return x * flag
        while x >= 10:
            ret *= 10
            ret += x % 10
            x = x // 10
        if ret > int_max//10 or \
                (ret == int_max // 10 and x > int_max % 10 and flag == 1) or \
                (ret == int_max // 10 and x > (int_max % 10 + 1) and flag == -1):
            return 0
        return (ret * 10 + x) * flag


if __name__ == "__main__":
    solution = Solution()
    print( pow(2, 31) - 1)
    # print('-----------')
    # x = 123
    # print(x)
    # print(solution.reverse(x))
    # print(solution.reverse(x) == 321)
    # print('-----------')
    # x = -123
    # print(x)
    # print(solution.reverse(x))
    # print(solution.reverse(x) == -321)
    # print('-----------')
    # x = 120
    # print(x)
    # print(solution.reverse(x))
    # print(solution.reverse(x) == 21)
    # print('-----------')
    # x = 0
    # print(x)
    # print(solution.reverse(x))
    # print(solution.reverse(x) == 0)
    # print('-----------')
    # x = 10
    # print(x)
    # print(solution.reverse(x))
    # print(solution.reverse(x) == 1)
    print('-----------')
    x = -1463847412
    print(x)
    print(solution.reverse(x))
    print(solution.reverse(x) == -2147483641)
    print('-----------')
    x = -8463847412
    print(x)
    print(solution.reverse(x))
    print(solution.reverse(x) == -2147483648)
    print('-----------')
    x = -9463847412
    print(x)
    print(solution.reverse(x))
    print(solution.reverse(x) == -2147483649)
    print('-----------')

