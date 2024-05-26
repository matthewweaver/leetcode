#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        l = [word.strip() for word in l if word != '']
        l.reverse()
        return ' '.join(l)

# @lc code=end

sol = Solution()
print(sol.reverseWords("the sky is blue"))