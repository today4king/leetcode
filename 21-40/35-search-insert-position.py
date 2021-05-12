#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_l = len(nums)

        def partition(nums, target, start_i, end_j):

            middle = (start_i + end_j) // 2
            if nums[middle] == target:
                return middle
            if start_i == end_j:
                if nums[middle] > target:
                    return middle
                else:
                    return middle + 1
            if nums[middle] > target:
                if middle == 0 or (middle > start_i and nums[middle - 1] < target):
                    return middle
                return partition(nums, target, start_i, middle - 1)
            else:
                if middle == nums_l or (middle < end_j and nums[middle + 1] > target):
                    return middle+1
                return partition(nums, target, middle + 1, end_j)

        return partition(nums, target, 0, nums_l - 1)


solution = Solution()

nums = [1,3]
target = 2
print(solution.searchInsert(nums, target))
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))
nums = [1, 3, 5, 6]
target = 2
print(solution.searchInsert(nums, target))
nums = [1, 3, 5, 6]
target = 7
print(solution.searchInsert(nums, target))
nums = [1, 3, 5, 6]
target = 0
print(solution.searchInsert(nums, target))
nums = [1]
target = 0
print(solution.searchInsert(nums, target))
