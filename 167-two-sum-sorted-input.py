#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

from memory_profiler import profile


class Solution:

    def twoSum(self, numbers, target) -> [int]:
        t = target
        j = len(numbers) - 1
        i = 0
        while not numbers[i] + numbers[j] == t:
            if numbers[i] + numbers[j] > t:
                j -= 1
            else:
                i += 1

        return [i + 1, j + 1]


# @profile
def inspect(nums, t):
    ds = Solution().twoSum(nums, t)
    print(ds)


if __name__ == "__main__":
    # inspect([2, 7, 11, 15], 9)
    # inspect([2,3,4], 6)
    # inspect([-1, 0], -1)
    inspect([3, 24, 50, 79, 88, 150, 345], 200)
