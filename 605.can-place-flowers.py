#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = [0] * len(flowerbed)
        for i, plot in enumerate(flowerbed):
            # unless current plot has flower
            if plot == 1:
                continue
            # unless plot in front has flower
            if i < len(flowerbed) - 1 and flowerbed[i+1] != 0:
                continue
            # unless plot behind has flower
            if i > 0 and (planted[i-1] != 0 or flowerbed[i-1] != 0):
                continue
            planted[i] = 1

        print(flowerbed)
        print(planted)
        if sum(planted) >= n:    
            return True
        return False


# @lc code=end

sol = Solution()
print(sol.canPlaceFlowers([0,0,1,0,1],1))