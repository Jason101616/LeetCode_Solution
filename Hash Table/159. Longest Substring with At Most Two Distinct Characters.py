# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

# For example, Given s = “eceba”,

# T is "ece" which its length is 3.


# idea: maintain a hashtable, with key is character, value is the number of time it appear in the substring
# also maintain a left pointer, if the number of element in the dictionary is larger than 2, the left pointer will be responsible for deleting some characters
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_cnt = collections.defaultdict(lambda: 0)
        left = 0
        max_len = 0
        for i in range(len(s)):
            char_cnt[s[i]] += 1
            while len(char_cnt) > 2:
                char_cnt[s[left]] -= 1
                if char_cnt[s[left]] == 0:
                    del char_cnt[s[left]]
                left += 1
            max_len = max(max_len, i - left + 1)
        return max_len