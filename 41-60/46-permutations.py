#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_permute(nums):
            l = len(nums)
            if l == 1:
                return [nums]
            ret = []
            n = nums[0]
            for a in get_permute(nums[1:]):
                for i in range(l):
                    r = []
                    for j, c in enumerate(a):
                        if i == j:
                            r.append(n)
                        r.append(c)
                    if i == l - 1:
                        r.append(n)
                    ret.append(r)
            return ret

        return get_permute(nums)


solution = Solution()
nums = [1, 2, 3]
print(solution.permute(nums))

nums = [0, 1]
print(solution.permute(nums))

nums = [1]
print(solution.permute(nums))
