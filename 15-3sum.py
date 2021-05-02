#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import *


class Solution:
    def sort(self, nums: List[int], start, end):
        is_from_right = True
        i = start
        j = end
        pivot = start
        while j > i:
            if is_from_right and nums[j] < nums[i]:
                # swap
                nums[j] += nums[i]
                nums[i] = nums[j] - nums[i]
                nums[j] = nums[j] - nums[i]
                i += 1
                is_from_right = False
                pivot = j
            if not is_from_right and nums[i] > nums[j]:
                # swap
                nums[j] += nums[i]
                nums[i] = nums[j] - nums[i]
                nums[j] = nums[j] - nums[i]
                j -= 1
                is_from_right = True
                pivot = i
            if is_from_right:
                j -= 1
            else:
                i += 1
        if pivot > 1:
            nums = self.sort(nums, 0, pivot - 1)
        if pivot < end - 1:
            nums = self.sort(nums, pivot + 1, end)
        return nums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_l = len(nums)
        if nums_l < 3:
            return []
        return self.sort(nums,0,nums_l-1)


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(nums)
    print(solution.threeSum(nums))
    print(solution.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]])
    print('-------------------------------------')
    nums = []
    print(nums)
    print(solution.threeSum(nums))
    print(solution.threeSum(nums) == [])
    print('-------------------------------------')
