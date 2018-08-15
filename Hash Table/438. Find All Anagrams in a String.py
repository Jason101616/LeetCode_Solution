# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# Time: O(len(s) + len(p))
# Space: O(len(p))
# idea: sliding window.
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        cntP = Counter(p)
        numKeys = len(cntP)
        res = []
        l = r = 0
        while r < len(s):
            if s[r] in cntP:
                cntP[s[r]] -= 1
                if cntP[s[r]] == 0:
                    numKeys -= 1
                    if numKeys == 0:
                        res.append(l)
                elif cntP[s[r]] < 0:
                    while cntP[s[r]] < 0:
                        cntP[s[l]] += 1
                        if cntP[s[l]] == 1:
                            numKeys += 1
                        l += 1
                r += 1
                if r - l + 1 > len(p):
                    cntP[s[l]] += 1
                    if cntP[s[l]] == 1:
                        numKeys += 1
                    l += 1
            else:
                while l < r:
                    cntP[s[l]] += 1
                    if cntP[s[l]] == 1:
                        numKeys += 1
                    l += 1
                l = r = r + 1
                numKeys = len(cntP)
        return res


# a more concise solution, use Count in Python. But slower than previous solution.
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1  # include a new char in the window
            if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
        return res
