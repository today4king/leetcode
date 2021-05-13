#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        len_num1 = len(num1)
        len_num2 = len(num2)
        sum_list = []
        i = len_num2 - 1
        while i >= 0:
            if num2[i] == '0':
                i -= 1
                continue
            s = ''
            j = len_num1 - 1
            carry = 0
            while j >= 0:
                sn = int(num2[i]) * int(num1[j]) + carry
                s = str(sn % 10) + s
                carry = sn // 10
                j -= 1
            if carry > 0:
                s = str(carry) + s
            i_zero = len_num2 - 1 - i
            for z in range(i_zero):
                s += '0'
            sum_list.append(s)
            i -= 1

        def sum(x, y):
            l_x = len(x)
            l_y = len(y)
            i = 0
            carry = 0
            sum = ''
            while i < max(l_x, l_y):
                i_x = l_x - 1 - i
                i_y = l_y - 1 - i
                n_x = int(x[i_x]) if i_x >= 0 else 0
                n_y = int(y[i_y]) if i_y >= 0 else 0
                s = n_x + n_y + carry
                sum = str(s % 10) + sum
                carry = s // 10
                i += 1
            if carry > 0:
                sum = str(carry) + sum
            return sum

        i = 0
        s = None
        while i < len(sum_list):
            if s is None:
                s = sum_list[i]
                i += 1
                continue
            s = sum(s, sum_list[i])
            i += 1
        return s


solution = Solution()
num1 = "9"
num2 = "9"
print(solution.multiply(num1, num2))
num1 = "2"
num2 = "3"
print(solution.multiply(num1, num2))
num1 = "123"
num2 = "456"
print(solution.multiply(num1, num2))
num1 = "1000000000000000000000001"
num2 = "22222222222222222222"
print(solution.multiply(num1, num2))
