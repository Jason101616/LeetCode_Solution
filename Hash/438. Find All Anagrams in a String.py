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

# Time:  O(n)
# Space: O(1)
# idea: sliding window with character count
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        ret = []
        orda = ord('a')
        cnt_s, cnt_p = [0 for i in range(26)], [0 for i in range(26)]
        for i in range(len(p) - 1):
            cnt_s[ord(s[i]) - orda] += 1
            cnt_p[ord(p[i]) - orda] += 1
        cnt_p[ord(p[len(p) - 1]) - orda] += 1
        
        for i in range((len(p) - 1), len(s)):
            cnt_s[ord(s[i]) - orda] += 1
            if cnt_s == cnt_p:
                ret.append(i + 1 - len(p))
            cnt_s[ord(s[i + 1 - len(p)]) - orda] -= 1
        return ret
        