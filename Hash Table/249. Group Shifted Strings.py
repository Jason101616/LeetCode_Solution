# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# Example:
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]


from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        mapping = defaultdict(lambda: [])
        for string in strings:
            mapping[self.helper(string)].append(string)
        return list(mapping.values())

    def helper(self, string):
        if len(string) == 1:
            return ()
        minus = ord(string[0]) - ord('a')
        res = []
        for char in string:
            tmp = ord(char) - minus
            if tmp < ord('a'):
                res.append(tmp + 26)
            else:
                res.append(tmp)
        return tuple(res)
