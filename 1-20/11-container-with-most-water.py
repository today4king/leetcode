#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0
        last_min_h = 0
        while j > i:
            d = j - i
            if min(height[i], height[j])>last_min_h:
                last_min_h=min(height[i], height[j])
                this_area = d * min(height[i], height[j])
                area = max(area, this_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return area


if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(height)
    print(solution.maxArea(height))
    print(solution.maxArea(height) == 49)
    print('-------------------------------------')
    height = [1, 1]
    print(height)
    print(solution.maxArea(height))
    print(solution.maxArea(height) == 1)
    print('-------------------------------------')
    height = [4, 3, 2, 1, 4]
    print(height)
    print(solution.maxArea(height))
    print(solution.maxArea(height) == 16)
    print('-------------------------------------')
    height = [1, 2, 1]
    print(height)
    print(solution.maxArea(height))
    print(solution.maxArea(height) == 2)
    print('-------------------------------------')
