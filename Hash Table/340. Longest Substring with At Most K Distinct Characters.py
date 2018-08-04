# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# For example, Given s = “eceba” and k = 2,

# T is "ece" which its length is 3.


# the same idea as 159 Longest Substring with At Most Two Distinct Characters
# idea: maintain a hashtable, with key is character, value is the number of time it appear in the substring
# also maintain a left pointer, if the number of element in the dictionary is larger than 2, the left pointer will be responsible for deleting some characters
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s_cnt = collections.defaultdict(lambda: 0)
        left = 0
        longest = 0
        for index, char in enumerate(s):
            s_cnt[char] += 1
            while len(s_cnt) > k:
                s_cnt[s[left]] -= 1
                if s_cnt[s[left]] == 0:
                    del s_cnt[s[left]]
                left += 1
            if index - left + 1 > longest:
                longest = index - left + 1
        return longest
