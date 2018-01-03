# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Examples:
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.

# time: O(m * (n-1)Cm), where n is the length of pattern, m is the length of str
# C means combination, (n-1)Cm = C(n-1)m
# idea: backtracking, use any length in the str to mapping one char
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mapping = {}
        string_set = set()
        return self.is_mapping(pattern, 0, str, 0, mapping, string_set)
    
    def is_mapping(self, pattern, p_i, str, s_i, mapping, string_set):
        if p_i == len(pattern) and s_i == len(str):
            return True
        if p_i == len(pattern) or s_i == len(str):
            return False
        
        if pattern[p_i] in mapping:
            # check whether previous mapping equals to the current string snippet
            len_str = len(mapping[pattern[p_i]])
            if str[s_i: s_i + len_str] != mapping[pattern[p_i]]:
                return False
            else:
                return self.is_mapping(pattern, p_i + 1, str, s_i + len_str, mapping, string_set)
        else:
            # backtracking
            for i in range(s_i, len(str)):
                sub_str = str[s_i:i + 1]
                if sub_str in string_set:
                    continue
                mapping[pattern[p_i]] = sub_str
                string_set.add(sub_str)
                if self.is_mapping(pattern, p_i + 1, str, i + 1, mapping, string_set):
                    return True
                string_set.remove(sub_str)
                del mapping[pattern[p_i]]
        return False
