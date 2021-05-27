#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        def get_permuteUnique(nums):
            if len(nums) == 1:
                return [nums]
            ret = {}
            num = nums[0]
            sub_pus = get_permuteUnique(nums[1:])
            for sub_nums in sub_pus:
                for i in range(len(sub_nums)):
                    if i > 0 and sub_nums[i - 1] == num:
                        continue
                    new_sn = sub_nums.copy()
                    new_sn.insert(i, num)
                    ret[str(new_sn)]=new_sn

                if sub_nums[-1] == num:
                    continue
                ret[str(sub_nums + [num])] = sub_nums + [num]
            return list(ret.values())

        return get_permuteUnique(nums)


solution = Solution()
nums = [1, 1, 2]
print(nums)
print(solution.permuteUnique(nums))

nums = [1,2,3]
print(nums)
print(solution.permuteUnique(nums))