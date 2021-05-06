#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 0:
            return 0
        nflag = 1
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0:
            nflag = -1
            dividend = -dividend
        elif divisor < 0:
            nflag = -1
            divisor = -divisor
        if dividend < divisor:
            return 0
        i = 0
        d_list = [divisor]
        sum_list = [1]
        while dividend > d_list[i]:
            d_list.append(d_list[i] + d_list[i])
            sum_list.append(sum_list[i] + sum_list[i])
            i += 1

        ret = 0
        while dividend > 0 and i >= 0:
            if dividend < d_list[i]:
                i -= 1
                continue
            dividend -= d_list[i]
            ret += sum_list[i]

        ret = ret if nflag > 0 else -ret
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)
        if ret > int_max:
            ret = int_max
        elif ret < int_min:
            ret = int_min
        return ret


solution = Solution()
dividend = 10
divisor = 3
print(solution.divide(dividend, divisor))
print('--------------')
dividend = 7
divisor = -3
print(solution.divide(dividend, divisor))
print('--------------')
dividend = 0
divisor = 1
print(solution.divide(dividend, divisor))
print('--------------')
dividend = 1
divisor = 1
print(solution.divide(dividend, divisor))
print('--------------')
dividend = 1234
divisor = 2
print(solution.divide(dividend, divisor))
print('--------------')
dividend = -2147483648
divisor = -1
print(solution.divide(dividend, divisor))
print('--------------')
