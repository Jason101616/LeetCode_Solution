# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# KMP is the best. This is only brute force.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if self.helper(haystack, needle, i):
                return i
        return -1

    def helper(self, haystack, needle, idx):
        for i in range(idx, idx + len(needle)):
            if haystack[i] != needle[i - idx]:
                return False
        return True
