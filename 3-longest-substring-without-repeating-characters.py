from memory_profiler import profile


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        MaxL = 0
        ss = []
        for i, c in enumerate(s):

            if ss.__contains__(c):
                repeat_i = ss.index(c)
                ss = ss[repeat_i + 1:]
                ss.append(c)
            else:
                ss.append(c)
            if len(ss) > MaxL:
                MaxL = len(ss)
        return MaxL



@profile
def inspect(s, l):
    L = Solution().lengthOfLongestSubstring(s)
    print('%s\tLength %d\tEspected %d' % (L == l, L, l))


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb") == 3)
    print(Solution().lengthOfLongestSubstring("bbbbb") == 1)
    print(Solution().lengthOfLongestSubstring("pwwkew") == 3)
    print(Solution().lengthOfLongestSubstring("dvdf") == 3)
    print(Solution().lengthOfLongestSubstring(" ") == 1)
    inspect("aabaab!bb", 3)

# 10.5MB
