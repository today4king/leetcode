#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = nums_l = len(nums)
        i = j = 0
        while j < nums_l:
            if nums[i] == val:
                nums.pop(i)
                l -= 1
            else:
                i += 1
            j += 1
        return l


solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
