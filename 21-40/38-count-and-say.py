#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            s = self.countAndSay(n - 1)
            new_s = [-1] * (len(s)*2+1)
            j = 0
            for i, c in enumerate(s):

                if i == 0:
                    new_s[j] = 1
                elif s[i - 1] == c:
                    new_s[j] += 1
                elif s[i - 1] != c:
                    j += 1
                    new_s[j] = int(s[i - 1])
                    j += 1
                    new_s[j] = 1

            new_s[j + 1] = int(s[-1])
            ret = ''
            for n in new_s:
                if n > 0:
                    ret += str(n)
            return ret


solution = Solution()
n = 1
print(solution.countAndSay(n))
n = 2
print(solution.countAndSay(n))
n = 3
print(solution.countAndSay(n))
n = 4
print(solution.countAndSay(n))
n = 5
print(solution.countAndSay(n))
n = 10
print(solution.countAndSay(n))
