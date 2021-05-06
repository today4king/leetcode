#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l_nums = len(nums)
        ret = []
        if l_nums < 4:
            return ret
        nums = sorted(nums)
        for i in range(l_nums - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, l_nums - 2):
                if j > 1 and j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                x = j + 1
                y = l_nums - 1
                while y > x:
                    diff = nums[i] + nums[j] + nums[y] + nums[x] - target
                    if diff == 0:
                        ret.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        while nums[x] == nums[x - 1] and y > x:
                            x += 1
                        y -= 1
                        while nums[y] == nums[y + 1] and y > x:
                            y -= 1
                    elif diff > 0:
                        y -= 1
                    else:
                        x += 1
        return ret


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    print(nums)
    print(solution.fourSum(nums, 0))
    print(solution.fourSum(nums, 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    print('---------------------')
    nums = [2, 2, 2, 2, 2]
    print(nums)
    print(solution.fourSum(nums, 8))
    print(solution.fourSum(nums, 8) == [[2, 2, 2, 2]])
    print('---------------------')
    nums = [-2, -1, -1, 1, 1, 2, 2]
    print(nums)
    print(solution.fourSum(nums, 0))
    print(solution.fourSum(nums, 0) == [[-2, -1, 1, 2], [-1, -1, 1, 1]])
    print('---------------------')
