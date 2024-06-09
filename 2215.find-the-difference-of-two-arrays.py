#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#


# @lc code=start
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        distinct_set_1 = set(nums1)
        distinct_set_2 = set(nums2)
        distinct_list_1 = [n for n in distinct_set_1 if n not in distinct_set_2]
        distinct_list_2 = [n for n in distinct_set_2 if n not in distinct_set_1]
        return [distinct_list_1, distinct_list_2]


# @lc code=end
