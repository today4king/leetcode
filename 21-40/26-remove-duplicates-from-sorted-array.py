#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_nums = len(nums)
        l = i = 0
        while l < l_nums:
            if i > 0 and nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
            l += 1
        return len(nums)

solution=Solution()
print(solution.removeDuplicates([1,1,2]))
print(solution.removeDuplicates( [0,0,1,1,1,2,2,3,3,4]))