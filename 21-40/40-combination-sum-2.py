#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class TreeNode():
    def __init__(self, val, candidates, path=None, parent=None):
        self.parent = parent
        self.val = val
        self.path = path
        self.children = []
        if self.val > 0:
            for i, c in enumerate(candidates):
                if i + 1 < len(candidates):
                    new_candidtes = candidates[i + 1:]
                else:
                    new_candidtes = []
                self.children.append(TreeNode(val - c, new_candidtes, c, self))
                if val - c <= 0:
                    break


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # pre inspect too big
        sum=0
        for n in candidates:
            sum+=n
        if target>sum:
            return []
        elif target==sum:
            return [candidates]
        candidates = sorted(candidates)
        root = TreeNode(target, candidates)
        ret= self.combineNode(root)
        no_dup={}
        for r in ret:
            k=''
            for n in r:
               k+=str(n)
            no_dup[k]=r
        return list(no_dup.values())

    def combineNode(self, node: TreeNode):
        ret = []
        if node.val < 0:
            return []
        if node.val == 0:
            return [[node.path]]

        for c in node.children:
            for r in self.combineNode(c):
                if node.path is not None:
                    ret.append([node.path] + r)
                else:
                    ret.append(r)
        return ret


solution = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(solution.combinationSum2(candidates, target))

candidates = [2, 5, 2, 1, 2]
target = 5
print(solution.combinationSum2(candidates, target))

candidates = [2, 3, 6, 7]
target = 7
print(solution.combinationSum2(candidates, target))


candidates =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
print(solution.combinationSum2(candidates, target))
