#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import  List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_letters='abcdefghijklmnopqrstuvwxyz'
        letters_dic={}
        for i,c in enumerate(all_letters):
            letters_dic[c]=i
        group_dic={}

        for s in strs:
            letters_map = [0] * 26
            for c in s:
                letters_map[letters_dic[c]]+=1
            if str(letters_map) in group_dic:
                group_dic[str(letters_map)].append(s)
            else:
                group_dic[str(letters_map)]=[s]
        return list(group_dic.values())
solution=Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(strs)
print(solution.groupAnagrams(strs))
strs = [""]
print(strs)
print(solution.groupAnagrams(strs))
strs = ["e"]
print(strs)
print(solution.groupAnagrams(strs))

strs = ["ddddddddddg","dgggggggggg"]
print(strs)
print(solution.groupAnagrams(strs))