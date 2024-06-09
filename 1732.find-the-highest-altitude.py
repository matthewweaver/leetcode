#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#


# @lc code=start
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(altitude, max_altitude)
        return max_altitude


# @lc code=end
