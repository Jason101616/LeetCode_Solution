# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    # 思路：暴力匹配。可以不用kmp算法。
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        j = -1
        for _ in range(len_haystack - len_needle + 1):
            for __ in range(len_needle):
                if haystack[_ + __] != needle[__]:
                    break
                j = __
            if j == len_needle - 1:
                return _
        return -1
    