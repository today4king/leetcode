#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_l=len(nums)
        if nums[0]==0:
            return False

        i=nums_l
        while i>=0:
            i-=1
            n=nums[i]
            if n==0:
                last_valid_jump=nums_l
                is_cross=False
                for j in range(i):
                    jump=nums[nums_l-i-2]
                    if jump+nums_l-i-2 >nums_l-i-1:
                        is_cross=True
                        if nums_l - i - 2 <last_valid_jump:
                            last_valid_jump=nums_l - i - 2
                if not is_cross:
                    return False


