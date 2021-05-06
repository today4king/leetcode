#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        nums_l = len(nums)
        closest_sum = nums[0] + nums[1] + nums[nums_l - 1]

        for i in range(nums_l - 2):
            # skip dunplicate num
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            x = i + 1
            y = nums_l - 1
            begin_distance = -1
            while y > x:
                sum = nums[i] + nums[x] + nums[y]
                diff = nums[i] + nums[x] + nums[y] - target
                if begin_distance < 0:
                    begin_distance = abs(diff)
                if abs(diff) < abs(closest_sum - target):
                    closest_sum = sum
                if abs(diff) <= begin_distance:
                    begin_distance = abs(diff)
                if diff == 0:
                    break
                elif diff > 0:
                    y -= 1
                else:
                    x += 1

        return closest_sum


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 2, 1, -4]
    print(nums)
    print(solution.threeSumClosest(nums, 1))
    print(solution.threeSumClosest(nums, 1) == 2)
    print('-------------------------------------')
    nums = [1, 1, 1, 0]
    print(nums)
    print(solution.threeSumClosest(nums, 100))
    print(solution.threeSumClosest(nums, 100) == 3)
    print('-------------------------------------')
    nums = [0, 1, 2]
    print(nums)
    print(solution.threeSumClosest(nums, 0))
    print(solution.threeSumClosest(nums, 0) == 3)
    print('-------------------------------------')
    nums = [0, 2, 1, -3]
    print(nums)
    print(solution.threeSumClosest(nums, 0))
    print(solution.threeSumClosest(nums, 0) == 0)
    print('-------------------------------------')
    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    print(nums)
    print(solution.threeSumClosest(nums, 82))
    print(solution.threeSumClosest(nums, 82) == 82)
    print('-------------------------------------')
    nums = [1, 2, 5, 10, 11]
    print(nums)
    print(solution.threeSumClosest(nums, 12))
    print(solution.threeSumClosest(nums, 12) == 13)
    print('-------------------------------------')
    nums = [-55, -24, -18, -11, -7, -3, 4, 5, 6, 9, 11, 23, 33]
    print(nums)
    print(solution.threeSumClosest(nums, 0))
    print(solution.threeSumClosest(nums, 0) == 0)
    print('-------------------------------------')


