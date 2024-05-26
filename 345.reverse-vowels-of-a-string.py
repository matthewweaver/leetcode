#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u'])
        vowel_indices = []
        reversed = list(s)
        for i, letter in enumerate(s):
            if letter.lower() in vowels:
                vowel_indices.append(i)
        count = 1
        for j in vowel_indices:
            reversed_index = vowel_indices[-count]
            reversed[j] = s[reversed_index] 
            count += 1
        return "".join(reversed)
# @lc code=end

sol = Solution()
print(sol.reverseVowels("aA"))