#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 1
        current_p = 0
        for n in arr:
            while  s < n and current_p < k:
                s += 1
                current_p += 1
            if current_p == k:
                return s-1
            s += 1
        while current_p < k:
            s += 1
            current_p += 1
        return s-1

solution=Solution()
nums=[1,2,3,4]
print(solution.findKthPositive(nums,2))
nums=[1,2]
print(solution.findKthPositive(nums,1))
