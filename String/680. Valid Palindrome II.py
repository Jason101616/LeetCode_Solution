# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# 思路1：删除任意一个char，然后验证是否是回文。会超时。
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self.isValidPalindrome(s):
            return True

        for index in range(len(s)):
            substr = s[0: index] + s[index + 1:]
            if self.isValidPalindrome(substr):
                return True

        return False

    def isValidPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


# 思路2：判断回文蕴含着这样一个递归关系式

# validPalindrome(s, i, j) = {
#     if s[i] == s[j]:
#         validPalindrome(s, i + 1, j - 1)
#     else:
#         is_valid_Palindrome(s, i + 1, j) or is_valid_Palindrome(s, i, j - 1)
# }

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j = len(s) - 1
        for i in range(len(s) / 2):
            if s[i] != s[j]:
                return self.isValidPalindrome(s, i, len(s) - 2 - i) or self.isValidPalindrome(s, i + 1, len(s) - 1 - i)
            else:
                i += 1
                j -= 1

        return True

    def isValidPalindrome(self, s, i, j):
        left = i
        right = j
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
