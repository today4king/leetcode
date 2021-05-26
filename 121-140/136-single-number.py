#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import  List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic_pair = {}
        for n in nums:
            if n in dic_pair:
                dic_pair[n] = 0
            else:
                dic_pair[n] = 1
        for k, v in dic_pair.items():
            if v == 1:
                return k
