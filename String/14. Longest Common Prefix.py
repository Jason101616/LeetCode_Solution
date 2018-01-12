# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            res = self.get_common_prefix_two_strings(res, strs[i])
        return res
    
    def get_common_prefix_two_strings(self, string1, string2):
        res = []
        if len(string2) > len(string1):
            string1, string2 = string2, string1
        for i in range(len(string2)):
            if string1[i] != string2[i]:
                break
            res.append(string2[i])
        return ''.join(res)
        