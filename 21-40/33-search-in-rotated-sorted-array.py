#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_l = len(nums)

        def binarySearch(nums, start, end, target):
            if end < start: return -1
            # order part
            if nums[end] - nums[start] == end - start:
                if target < nums[start] or target > nums[end]:
                    return -1
                else:
                    return target - nums[start] + start
            # cut to 2
            middle = (end + start) // 2
            if nums[middle] == target:
                return middle
            elif middle == 0 and middle == end:
                return -1

            if middle > 0:
                left = binarySearch(nums, start, middle - 1, target)
                if left >= 0:
                    return left

            right = binarySearch(nums, middle + 1, end, target)
            if right >= 0:
                return right
            return -1

        return binarySearch(nums, 0, nums_l - 1, target)


solution = Solution()

nums = [7, 9, 1, 4, 6]
target = 5
print(solution.search(nums, target))
nums = [3, 4, 5, 6, 1, 2]
target = 2
print(solution.search(nums, target))
nums = [1, 3, 5]
target = 1
print(solution.search(nums, target))
nums = [1, 3]
target = 3
print(solution.search(nums, target))
nums = [1, 3]
target = 0
print(solution.search(nums, target))
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(solution.search(nums, target))
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(solution.search(nums, target))
nums = [1]
target = 0
print(solution.search(nums, target))
