#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        p = 0
        if x % 10 == 0:
            return False
        while x > p:
            p = p * 10 + x % 10
            if p == x:
                return True
            x //= 10
            if p == x:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    s = 121
    print(solution.isPalindrome(s))
    print('--------------------------------')
    s = -121
    print(solution.isPalindrome(s))
    print('--------------------------------')
    s = 10
    print(solution.isPalindrome(s))
    print('--------------------------------')
    s = -101
    print(solution.isPalindrome(s))
    print('--------------------------------')
    s = 121121
    print(solution.isPalindrome(s))
    print('--------------------------------')
