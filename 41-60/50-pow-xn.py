#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)

        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x, n - 1)


solution = Solution()
x = 2.00000
n = 10
print('x=%d\tn=%d' % (x, n))
print(solution.myPow(x, n))
print(solution.myPow(x, n) == 1024.00000)
x = 2.10000
n = 3
print('x=%d\tn=%d' % (x, n))
print(solution.myPow(x, n))
print(solution.myPow(x, n) == 9.26100)
x = 2.00000
n = -2
print('x=%d\tn=%d' % (x, n))
print(solution.myPow(x, n))
print(solution.myPow(x, n) == 0.25000)

x = 0.00001
n = 2147483647
print('x=%d\tn=%d' % (x, n))
print(solution.myPow(x, n))
print(solution.myPow(x, n) == 0)
