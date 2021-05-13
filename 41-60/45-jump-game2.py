#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class TreeNode():
    def __init__(self, nums, index, depth=None, parent=None):
        self.parent = parent
        self.val = index

        self.children = []
        if self.val < len(nums) - 1 and nums[index] > 0:
            for i in range(nums[index]):
                current_i = i + self.val + 1
                if current_i < len(nums):
                    if nums[current_i]+current_i>len(nums)-1 or nums[current_i]+current_i>nums[index]+index :
                        self.children.append(TreeNode(nums, current_i, depth + 1, self))
                else:
                    break
        if len(self.children) == 0 and index != len(nums) - 1:
            self.depth = -1
        else:
            self.depth = depth

    def minDepth(self):
        if len(self.children) == 0:
            return self, self.depth
        n, min_d = None, -1
        for c in self.children:
            c_min, c_min_d = c.minDepth()
            if c_min_d > 0 and (c_min_d < min_d or min_d < 0):
                min_d = c_min_d
                n = c_min
        return n, min_d


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if len(nums) <= 1:
            return 0

        if len(nums) == 2:
            return 1
        root = TreeNode(nums, 0, 0, None)
        n, d = root.minDepth()
        s = ''
        while  n.parent :
            s += '\t' + str(nums[n.val])
            n = n.parent
        s += '\t' + str(nums[n.val])
        print(s)
        return d


solution = Solution()

nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print(solution.jump(nums))
nums = [2, 3, 1, 1, 4]
print(solution.jump(nums))
nums = [2, 3, 0, 1, 4]
print(solution.jump(nums))

nums = [2, 2, 0, 1]
print(solution.jump(nums))

nums = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]
print(solution.jump(nums))

nums = [1,3,2]
print(solution.jump(nums))