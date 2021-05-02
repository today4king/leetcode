#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import *


class Solution:

    def has_k(self, i, j, k_value, nums):
        ks = []
        for n in nums[i+1:j]:
            if n == k_value:
                ks.append(n)
        return ks

    def sort(self, nums: List[int], start, end, coodinate_list):
        is_from_right = True
        i = start
        j = end
        pivot = start
        while j > i:
            if is_from_right and nums[j] < nums[i]:
                # swap number
                nums[j] += nums[i]
                nums[i] = nums[j] - nums[i]
                nums[j] = nums[j] - nums[i]
                # swap coodinate
                coodinate_list[j] += coodinate_list[i]
                coodinate_list[i] = coodinate_list[j] - coodinate_list[i]
                coodinate_list[j] = coodinate_list[j] - coodinate_list[i]
                i += 1
                is_from_right = False
                pivot = j
            if not is_from_right and nums[i] > nums[j]:
                # swap
                nums[j] += nums[i]
                nums[i] = nums[j] - nums[i]
                nums[j] = nums[j] - nums[i]
                # swap coodinate
                coodinate_list[j] += coodinate_list[i]
                coodinate_list[i] = coodinate_list[j] - coodinate_list[i]
                coodinate_list[j] = coodinate_list[j] - coodinate_list[i]
                j -= 1
                is_from_right = True
                pivot = i
            if is_from_right:
                j -= 1
            else:
                i += 1
        if pivot > 1:
            nums, coodinate_list = self.sort(nums, 0, pivot - 1, coodinate_list)
        if pivot < end - 1:
            nums, coodinate_list = self.sort(nums, pivot + 1, end, coodinate_list)
        return nums, coodinate_list

    def find_match(self, i, j, sorted_nums, coodinate_list):
        ret = []
        while j > i + 1:
            kv = 0 - sorted_nums[i] - sorted_nums[j]
            if kv > nums[j]:
                j -= 1
            elif kv < nums[i]:
                i += 1
            else:
                ks = self.has_k(i, j, kv, sorted_nums)
                for k in ks:
                    ret.append([coodinate_list[i], coodinate_list[k], coodinate_list[j]])
                for c in self.find_match(i + 1, j, sorted_nums, coodinate_list):
                    ret.append(c)
                for c in self.find_match(i, j - 1, sorted_nums, coodinate_list):
                    ret.append(c)
                i += 1
                j -= 1
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_l = len(nums)
        if nums_l < 3:
            return []
        coodinate_list = [x for x in range(len(nums))]
        sorted_nums, coodinate_list = self.sort(nums, 0, nums_l - 1, coodinate_list)
        i = 0
        j = nums_l - 1
        return self.find_match(i, j, sorted_nums, coodinate_list)


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
