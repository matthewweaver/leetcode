#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = [0] * len(flowerbed)
        for i, plot in enumerate(flowerbed):
            if plot == 1:
                pass
            else:
                if flowerbed[i+1] == 0:
                    if i>0:
                        if planted[i-1] == 0:
                            planted[i] = 1
                    else:
                        planted[i] = 1
        if sum(planted) >= n:
            return True
        return False


# @lc code=end

