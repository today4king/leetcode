#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

#5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print(s)
    print(solution.longestPalindrome(s)=="bab")
    s = "cbbd"
    print(s)
    print(solution.longestPalindrome(s) == "bb")
    s = "a"
    print(s)
    print(solution.longestPalindrome(s) == "a")
    s = "ac"
    print(s)
    print(solution.longestPalindrome(s) == "a")