
#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # pre process
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return 1
        border = 0
        jump = 0
        for i, c in enumerate(nums):
            if nums[i] + i > border:
                new_border = nums[i] + i
                if new_border > len(nums) - 1:
                    jump += 1
                    break
                while nums[new_border] == 0:
                    new_border -= 1
                border = new_border
                jump += 1

        return jump-1


solution = Solution()

nums = [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3,
        8, 5]
print(solution.jump(nums))
nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
print(solution.jump(nums))
nums = [2, 3, 1, 1, 4]
print(solution.jump(nums))
nums = [2, 3, 0, 1, 4]
print(solution.jump(nums))

nums = [2, 2, 0, 1]
print(solution.jump(nums))

nums = [2, 9, 6, 5, 7, 0, 7, 2, 7, 9, 3, 2, 2, 5, 7, 8, 1, 6, 6, 6, 3, 5, 2, 2, 6, 3]
print(solution.jump(nums))

nums = [1, 3, 2]
print(solution.jump(nums))
