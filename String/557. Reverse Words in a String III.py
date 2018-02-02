# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(string, left, right):
            while left < right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
                
        if not s:
            return s
        s = list(s)
        l = 0
        for index, char in enumerate(s):
            if char == ' ':
                reverse(s, l, index - 1)
                l = index + 1
        reverse(s, l, len(s) - 1)
        return ''.join(s)