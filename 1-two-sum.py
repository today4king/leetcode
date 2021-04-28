#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

from memory_profiler import profile


class Solution:

    def twoSum(self, nums, target) -> [int]:
        l = len(nums)
        for i, x in enumerate(nums):
            print(i, x)
            for j in range(i + 1, l):
                y = nums[j]
                print(j, y)
                if target == x + y:
                    return i, j


@profile
def inspect(nums, t):
    ds = Solution().twoSum(nums, t)
    print(ds)


if __name__ == "__main__":
    inspect([2, 7, 11, 15], 9)
    inspect([3,2,4], 6)
    inspect([3,3], 6)
