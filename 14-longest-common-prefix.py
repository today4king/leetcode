#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_l = len(strs)
        if strs_l == 1:
            return strs[0]
        i = 0
        j = 0
        comman_pre = ''
        while i < len(strs[j % strs_l]):
            if strs[j % strs_l][i] != strs[0][i]:
                break
            if j % strs_l == strs_l - 1:
                comman_pre += strs[j % strs_l][i]
                i += 1
            j += 1
        return comman_pre


if __name__ == "__main__":
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(strs)
    print(solution.longestCommonPrefix(strs))
    print(solution.longestCommonPrefix(strs) == 'fl')
    print('-------------------------------------')
    strs = ["dog", "racecar", "car"]
    print(strs)
    print(solution.longestCommonPrefix(strs))
    print(solution.longestCommonPrefix(strs) == '')
    print('-------------------------------------')
