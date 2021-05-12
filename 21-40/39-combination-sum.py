#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List
class TreeNode():
    def __init__(self,val,candidates,path=None,parent=None):
        self.parent=parent
        self.val=val
        self.path=path
        self.children=[]
        if self.val>0 :
            for i,c in enumerate(candidates):
                self.children.append(TreeNode(val-c,candidates[i:],c,self))
                if val-c<=0:
                    break

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates=sorted(candidates)
        root=TreeNode(target,candidates)
        return self.combineNode(root)

    def combineNode(self,node:TreeNode):
        ret=[]
        if node.val<0 :
            return []
        if node.val==0:
            return [[node.path]]

        for c in node.children:
            for r in  self.combineNode(c):
                if node.path is not None:
                    ret.append([node.path]+r)
                else:
                    ret.append(  r)
        return ret

solution=Solution()
candidates = [2,3,6,7]
target = 7
print(solution.combinationSum(candidates,target))
candidates = [2,3,5]
target = 8
print(solution.combinationSum(candidates,target))
candidates = [2]
target = 1
print(solution.combinationSum(candidates,target))
candidates = [1]
target = 1
print(solution.combinationSum(candidates,target))
candidates = [1]
target = 2
print(solution.combinationSum(candidates,target))

