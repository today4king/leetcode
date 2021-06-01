#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import List
import queue


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        for i, n in enumerate(nums):
            if i==0:
                ans = nums[0]
                sum = nums[0]
            else:
                if sum > 0:
                    sum += n
                else:
                    sum = n
                ans = ans if ans > sum else sum
        return ans


solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(nums)
print(solution.maxSubArray(nums))
print(solution.maxSubArray(nums) == 6)
nums = [1]
print(nums)
print(solution.maxSubArray(nums))
print(solution.maxSubArray(nums) == 1)
nums = [5, 4, -1, 7, 8]
print(nums)
print(solution.maxSubArray(nums))
print(solution.maxSubArray(nums) == 23)
