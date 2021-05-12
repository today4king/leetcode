#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_l = len(haystack)
        needle_l = len(needle)
        if needle == '' or haystack==needle:
            return 0
        if haystack_l < needle_l:
            return -1
        for i in range( haystack_l - needle_l+1):
            for j, c in enumerate(needle):
                if haystack[i + j] == needle[j]:
                    if j == needle_l - 1:
                        return i
                    else:
                        continue
                else:
                    break
        return -1


solution = Solution()
haystack = "hello"
needle = "ll"
print(solution.strStr(haystack, needle))
haystack = "aaaaa"
needle = "bba"
print(solution.strStr(haystack, needle))
haystack = ""
needle = ""
print(solution.strStr(haystack, needle))
haystack = "a"
needle = ""
print(solution.strStr(haystack, needle))
haystack = "a"
needle = "a"
print(solution.strStr(haystack, needle))
haystack = "abc"
needle = "c"
print(solution.strStr(haystack, needle))