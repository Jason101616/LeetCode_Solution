# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

# 一位位比较即可
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftIdx, rightIdx = 0, len(s) - 1
        while leftIdx < rightIdx:
            while leftIdx < len(s) and not s[leftIdx].isalnum():
                leftIdx += 1
            while rightIdx >= 0 and not s[rightIdx].isalnum():
                rightIdx -= 1
            if leftIdx >= rightIdx:
                return True
            if s[leftIdx].lower() != s[rightIdx].lower():
                return False
            leftIdx += 1
            rightIdx -= 1
        return True
