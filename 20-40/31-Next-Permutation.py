#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def closer(self, nums, start, end):
        i = end
        while i > start:
            j = i - 1
            while j >= start:
                if nums[i] > nums[j]:
                    if i > j + 1:
                        if nums[i]==nums[i-1]:
                            more_closer = self.closer(nums, j, i - 1)
                        else:
                            more_closer=self.closer(nums,j+1,i-1)
                        if more_closer is not None:
                            return more_closer
                    return j, i
                j -= 1
            i -= 1
        return None

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_l = len(nums)
        if nums_l == 1:
            return
        start_i = 0
        closest = self.closer(nums, 0, nums_l - 1)

        if closest:
            i, j = closest
            nums[i] = nums[i] + nums[j]
            nums[j] = nums[i] - nums[j]
            nums[i] = nums[i] - nums[j]
            start_i = i + 1
        i = start_i
        while i < nums_l - 1:
            j = i + 1
            while j < nums_l:
                if nums[j] < nums[i]:
                    nums[i] = nums[i] + nums[j]
                    nums[j] = nums[i] - nums[j]
                    nums[i] = nums[i] - nums[j]
                j += 1
            i += 1
        return


solution=Solution()
nums = [4, 2, 0, 2, 3, 2, 0]
print(nums)
solution.nextPermutation(nums)
print(nums)
print('----------------------')
nums = [1, 3, 2]
print(nums)
solution.nextPermutation(nums)
print(nums)
print('----------------------')
nums = [1, 2, 3]
print(nums)
solution.nextPermutation(nums)
print(nums)
print('----------------------')
nums = [3, 2, 1]
print(nums)
solution.nextPermutation(nums)
print(nums)
print('----------------------')
nums = [1, 1, 5]
print(nums)
solution.nextPermutation(nums)
print(nums)
print('----------------------')
nums = [1]
print(nums)
solution.nextPermutation(nums)
print(nums)
