#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#


# @lc code=start
from typing import List
import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            # Now first < num, if num <= second then try to make `second` as small as possible
            elif num <= second:
                second = num
            # Now first < second < num
            else:
                return True
        return False


# @lc code=end
