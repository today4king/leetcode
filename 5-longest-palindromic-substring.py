#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.simple_method(s)

    # 没有做完 abb这个案例似乎不适合马拉车算法
    def manacher(self,s):
        s_after = '$#' + '#'.join(list(s)) + '#^'
        p=[0]*len(s_after)
        max_p=0
        max_s=''
        for i,c in enumerate(s_after):
            p[i]=self.get_expand(s_after,i)
            if p[i]>max_p:
                max_p=p[i]
                max_s=s[i-p[i]-1::p[i]*2+1]
    def get_expand(self,s,i):
        pass


    def simple_method(self, s):
        s='$#'+'#'.join(list(s))+'#^'
        max_l = 0
        max_s = ''
        for i in range(len(s)):
            sp, l = self.sm_get_longest_palindrome(s, i)

            if l > max_l:
                max_l = l
                max_s = sp
        return max_s

    def sm_get_longest_palindrome(self, s, i):
        l = len(s)
        x = i - 1
        y = i + 1
        p = 1
        while x > -1 and y < l:
            if s[x] != s[y]:
                break
            x -= 1
            y += 1

        ps= s[i] if x+1==y-1 else s[x + 1:y-1]
        ps=ps.replace('#','').replace('$','').replace('^','')
        return ps,len(ps)


if __name__ == "__main__":
    s = Solution()
    print('babad')
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('babad') == "bab")
    print('cbbd')
    print(s.longestPalindrome('cbbd'))
    print(s.longestPalindrome('cbbd') == "bb")
    print('a')
    print(s.longestPalindrome('a'))
    print(s.longestPalindrome('a') == "a")
    print('ac')
    print(s.longestPalindrome('ac'))
    print(s.longestPalindrome('ac') == "a")
    print('ababaabc')
    print(s.longestPalindrome('ababaabc'))
    print(s.longestPalindrome('ababaabc') == "ababa")
    print('abb')
    print(s.longestPalindrome('abb'))
    print(s.longestPalindrome('abb') == "bb")
