#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
import random
from typing import *

from memory_profiler import profile


class Solution:

    def has_k(self, i, j, k_value, nums):

        for n in nums[i + 1:j]:
            if n == k_value:
                return True
        return False

    def swap(self, i, j, nums):
        nums[j] += nums[i]
        nums[i] = nums[j] - nums[i]
        nums[j] = nums[j] - nums[i]
        return nums

    def quick_sort(self, start, end, nums):
        if start < 0:
            return nums
        if end >= len(nums):
            return nums
        pivot = start
        i = start
        j = end
        # true from left, false from right
        right = True
        while j >= i:
            if right:
                if nums[j] < nums[pivot]:
                    nums = self.swap(i, j, nums)
                    pivot = j
                    right = False
                    i += 1
                else:
                    j -= 1
            else:
                if nums[i] > nums[pivot]:
                    nums = self.swap(i, j, nums)
                    pivot = i
                    right = True
                    j -= 1
                else:
                    i += 1
        if end > start:
            nums = self.quick_sort(start, pivot - 1, nums)
            nums = self.quick_sort(pivot + 1, end, nums)
        return nums

    def my_sort(self, nums: List[int]):
        return self.quick_sort(0, len(nums) - 1, nums)

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_l = len(nums)
        if nums_l < 3:
            return []
        sorted_nums = self.my_sort(nums)

        print(sorted_nums)
        i = 0
        ret = []
        while i < nums_l - 2:
            # 去除重复项
            if i > 1 and sorted_nums[i] == sorted_nums[i - 1]:
                i += 1
                continue
            # 排序后三个数中必定有负数
            if sorted_nums[i] > 0:
                break
            x = i + 1
            y = nums_l - 1
            while y > x:
                c = sorted_nums[x] + sorted_nums[y] + sorted_nums[i]
                if c == 0:
                    t = [sorted_nums[i], sorted_nums[x], sorted_nums[y]]
                    ret.append(t)
                    y -= 1
                    x += 1
                if c > 0:
                    y -= 1
                elif c < 0:
                    x += 1
            i += 1
        return ret


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
    nums = [0, 0, 0]
    print(nums)
    print(solution.threeSum(nums))
    print(solution.threeSum(nums) == [[0, 0, 0]])
    print('-------------------------------------')
    nums = [34, 55, 79, 28, 46, 33, 2, 48, 31, -3, 84, 71, 52, -3, 93, 15, 21, -43, 57, -6, 86, 56, 94, 74, 83, -14, 28,
            -66,
            46, -49, 62, -11, 43, 65, 77, 12, 47, 61, 26, 1, 13, 29, 55, -82, 76, 26, 15, -29, 36, -29, 10, -70, 69, 17,
            49]
    print(nums)
    print(solution.threeSum(nums))
    print(solution.threeSum(nums) == [[0, 0, 0]])
    print('-------------------------------------')
