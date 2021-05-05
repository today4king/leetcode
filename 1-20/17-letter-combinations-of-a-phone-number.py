#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List

l_dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


class Solution:
    def strComb(self, l_array: List[str], i: int):
        ret = []
        l_a = len(l_array)
        for c in l_array[i]:
            if l_a == i + 1:
                ret.append(c)
            else:
                for s in self.strComb(l_array, i + 1):
                    ret.append(c + s)
        return ret

    def letterCombinations(self, digits: str) -> List[str]:
        l_d = len(digits)
        if l_d == 0:
            return []

        l_array = []
        for c in digits:
            l_array.append(l_dic[c])
        ret = self.strComb(l_array, 0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    digits = "23"
    print(digits)
    print(solution.letterCombinations(digits))
    print(solution.letterCombinations(digits) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    print('---------------------')
    digits = ""
    print(digits)
    print(solution.letterCombinations(digits))
    print(solution.letterCombinations(digits) == [])
    print('---------------------')
    digits = "2"
    print(digits)
    print(solution.letterCombinations(digits))
    print(solution.letterCombinations(digits) == ["a", "b", "c"])
    print('---------------------')
    digits = "7"
    print(digits)
    print(solution.letterCombinations(digits))
    print(solution.letterCombinations(digits) == ["p", "q", "r", "s"])
    print('---------------------')
