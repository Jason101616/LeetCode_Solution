# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

# Time: O(l1 + l2), Space: O(1)
from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        ctr1 = Counter(s1)
        numOfChars = len(ctr1)
        ctr2 = {}
        l, r = 0, 0
        while r < len(s2):
            if s2[r] not in ctr1:
                r += 1
                ctr2 = {}
                numOfChars = len(ctr1)
                l = r
            else:
                if s2[r] not in ctr2:
                    ctr2[s2[r]] = 1
                else:
                    ctr2[s2[r]] += 1

                if ctr2[s2[r]] == ctr1[s2[r]]:
                    numOfChars -= 1
                    if numOfChars == 0:
                        return True
                elif ctr2[s2[r]] < ctr1[s2[r]]:
                    pass
                else:
                    while ctr2[s2[r]] > ctr1[s2[r]]:
                        ctr2[s2[l]] -= 1
                        if ctr2[s2[l]] == ctr1[s2[l]] - 1:
                            numOfChars += 1
                        l += 1
                r += 1
        return False
