#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_l=len(nums)
        if nums_l<3:
            return []


if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(nums)
    print(solution.threeSum(nums))
    print(solution.threeSum(nums) == [[-1,-1,2],[-1,0,1]])
    print('-------------------------------------')
    nums = []
    print(nums)
    print(solution.threeSum(nums))
    print(solution.threeSum(nums) == [])
    print('-------------------------------------')
