# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# time: O(n)
# space: O(n)
# idea: use dictionary and two pointers to calculate the number of each character
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt_num = defaultdict(lambda: 0)
        left, right, max_len = 0, 0, 0
        
        while right < len(s):
            cnt_num[s[right]] += 1
            while cnt_num[s[right]] > 1:
                cnt_num[s[left]] -= 1
                left += 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
            right += 1
        return max_len