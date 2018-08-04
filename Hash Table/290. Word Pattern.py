# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

# hash map, key is pattern, value is string snippet
# if key is not in the dict, check if string is in the values, if exist return false, else add the new mapping to the dict
# if key is in the dict, check whether the new mapping is consistent with the previous one
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        direct_mapping = {}
        string_set = set()
        string = str.split(' ')
        if len(pattern) != len(string):
            return False
        for index, char in enumerate(pattern):
            if char not in direct_mapping:
                if string[index] in string_set:
                    return False
                direct_mapping[char] = string[index]
                string_set.add(string[index])
            else:
                if direct_mapping[char] != string[index]:
                    return False
        return True
