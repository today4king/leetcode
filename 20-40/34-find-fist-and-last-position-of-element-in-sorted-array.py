
#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_l = len(nums)
        if nums_l == 0:
            return -1, -1

        def partition(nums, target, start_i, end_i):
            i = j = -1

            if nums[start_i] == target:
                i = start_i
            if nums[end_i] == target:
                j = end_i
            if i >= 0 and j >= 0:
                return i, j

            middle = (start_i + end_i) // 2
            if nums[middle] == target:
                if i < 0:
                    i = middle
                if j < 0:
                    j = middle
            if nums[middle] >= target and middle > start_i:
                left_i, left_j = partition(nums, target, start_i, middle - 1)
                if left_i > 0 and left_i < i:
                    i = left_i
                if left_j > 0 and left_j > j:
                    j = left_j
            if nums[middle] <= target and middle < end_i:
                right_i, right_j = partition(nums, target, middle + 1, end_i)
                if right_i > 0:
                    if i < 0:
                        i = right_i
                    elif right_i < i:
                        i = right_i
                if right_j > 0:
                    if j < 0:
                        j = right_j
                    elif right_j > j:
                        j = right_j

            return i, j

        start, end = partition(nums, target, 0, nums_l - 1)
        if start < 0:
            start = end
        if end < 0:
            end = start
        return start, end


solution = Solution()


nums = [0,0,1,1,1,2,3,4,4,5,6,7,7,7,8,8,8,8,9,9,10]
target = 4
#[7,8]
print(solution.searchRange(nums, target))
nums = [1,2,3]
target = 1
print(solution.searchRange(nums, target))
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(solution.searchRange(nums, target))
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(solution.searchRange(nums, target))
nums = []
target = 0
print(solution.searchRange(nums, target))