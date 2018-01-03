# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dict_pattern = collections.defaultdict(lambda: [])
        for string in strings:
            if len(string) == 1:
                dict_pattern[(0)].append(string)
                continue
            pattern = []
            for i in range(1, len(string)):
                if string[i] < string[i - 1]:
                    pattern.append(26 - (ord(string[i - 1]) - ord(string[i])))
                else:
                    pattern.append(ord(string[i]) - ord(string[i - 1]))
            dict_pattern[tuple(pattern)].append(string)
        res = []
        for pattern in dict_pattern.keys():
            res.append(dict_pattern[pattern])
        return res