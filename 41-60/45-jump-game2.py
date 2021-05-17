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

        is_continue = True
        i = len(nums) - 1
        j = -1
        last_found = False
        while is_continue:
            if i == len(nums) - 1:
                last_found = False
                print(nums)

            if nums[i] == 0 and i < len(nums) - 1 and nums[i + 1] != 0 or i + 1 == len(nums) - 1:
                j = i
            if i<j and nums[i] <= j - i :
                if nums[i]>0:
                    nums[i] = 0
                    last_found = True
            if nums[i] > j - i:
                j = -1

            if i > 0:
                i -= 1
            else:
                i = len(nums) - 1
            if i == 0 and last_found == False:
                is_continue = False
        max_border = 0
        jump = 0
        last_border=0
        for i, c in enumerate(nums):
            if nums[i] + i > max_border:
                new_border = nums[i] + i
                if new_border > len(nums) - 1:
                    print(i)
                    jump += 1
                    break
                elif new_border == len(nums) - 1:
                    print(i)
                    jump += 1
                    break

                while nums[new_border] == 0:
                    new_border -= 1
                if new_border>max_border:
                    max_border=new_border
            if last_border==0 or i ==last_border:
                last_border=max_border
                print(i)
                jump += 1

        return jump


solution = Solution()

nums = [1, 2, 3]
print(nums)
print(solution.jump(nums))
print(solution.jump(nums) == 2)

nums = [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3,
        8, 5]
print(nums)
print(solution.jump(nums))

nums = [3, 4, 3, 2, 5, 4, 3]
print(nums)
print(solution.jump(nums))
print(solution.jump(nums) == 3)

nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
print(nums)
print(solution.jump(nums))
print(solution.jump(nums) == 2)

nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
print(nums)
print(solution.jump(nums))
print(solution.jump(nums) == 3)

nums = [2, 3, 1, 1, 4]
print(nums)
print(solution.jump(nums))
print(solution.jump(nums) == 2)

nums = [2, 3, 0, 1, 4]
print(nums)
print(solution.jump(nums))
print(solution.jump(nums) == 2)

nums = [2, 2, 0, 1]
print(nums)
print(solution.jump(nums))
print(solution.jump(nums) == 2)

nums = [2, 9, 6, 5, 7, 0, 7, 2, 7, 9, 3, 2, 2, 5, 7, 8, 1, 6, 6, 6, 3, 5, 2, 2, 6, 3]
print(nums)
print(solution.jump(nums))

nums = [1, 3, 2]
print(nums)
print(solution.jump(nums))
