# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# time: O(n)
# space: O(n)
# idea: use dictionary and two pointers to calculate the number of each character
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l, r, res = 0, 0, 0
        charCnt = set()
        while r < len(s):
            if s[r] not in charCnt:
                charCnt.add(s[r])
                r += 1
                if r - l > res:
                    res = r - l
            else:
                while s[r] in charCnt:
                    charCnt.remove(s[l])
                    l += 1
        return res