#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisors = []
        substrings = []
        n1 = len(str1)
        n2 = len(str2)
        n_limit = max(n1, n2)
        for x in range(1, n_limit+1):
            if n1 % x == 0 and n2 % x == 0:
                divisors.append(x)
        for d in divisors:
            for s in [str1, str2]:
                substring = s[0:d]
                if substring*int(n1/d) == str1:
                    if substring*int(n2/d) == str2:
                        substrings.append(substring)
        if substrings:
            return max(substrings)
        else:
            return ""
        
# @lc code=end

# Local testing
sol = Solution()
sol.gcdOfStrings("LEET","CODE")