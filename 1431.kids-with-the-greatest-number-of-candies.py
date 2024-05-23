#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest = max(candies)
        for kid in candies:
            if kid + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
    
# @lc code=end

