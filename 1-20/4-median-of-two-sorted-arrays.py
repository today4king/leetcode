#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = self.conbime(nums1, nums2)
        print(nums3)
        l3 = len(nums3)
        end_num_count = 1 if l3 % 2 == 1 else 2
        if end_num_count == 1:
            return nums3[int(l3 / 2)]
        else:
            return int(nums3[int(l3 / 2)] + nums3[int(l3 / 2) - 1]) / 2

    def conbime(self,nums1, nums2):

        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0:
            return nums2
        if l2 == 0:
            return nums1
        nums3 = [0] * (l1 + l2)
        i1 = i2 = 0
        for i in range(l1 + l2):
            if i1 >= l1:
                nums3[i] = nums2[i2]
                i2 += 1
            elif i2 >= l2:
                nums3[i] = nums1[i1]
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                nums3[i] = nums2[i2]
                i2 += 1
            else:
                nums3[i] = nums1[i1]
                i1 += 1
        return nums3






if __name__ == "__main__":
    s=Solution()
    # S1
    nums1 = [1, 3]
    print(nums1)
    nums2 = [2]
    print(nums2)
    print(int(s.findMedianSortedArrays(nums1, nums2)) == 2)

    # S2
    nums1 = [1, 2]
    print(nums1)
    nums2 = [3, 4]
    print(nums2)
    print(int(s.findMedianSortedArrays(nums1, nums2)) == 2.5)

    # S3
    nums1 = [0, 0]
    print(nums1)
    nums2 = [0, 0]
    print(nums2)
    print(int(s.findMedianSortedArrays(nums1, nums2)) == 0)

    # S4
    nums1 = []
    nums2 = [1]
    print(int(s.findMedianSortedArrays(nums1, nums2)) == 1)

    # S5
    nums1 = [2]
    nums2 = []
    print(int(s.findMedianSortedArrays(nums1, nums2)) == 2)
