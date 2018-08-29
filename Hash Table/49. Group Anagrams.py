# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.

# Solution 1: use Counter in Python. Accepted but really slow.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(lambda: [])
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


# Solution 2: simply use the sorted string as the key
# Time Complexity: O(NKlog(K)), where N is the length of strs, and K is the maximum length of a string in strs.
# The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cnt_dict = collections.defaultdict(lambda: [])
        for s in strs:
            cnt_dict[tuple(sorted(s))].append(s)
        return cnt_dict.values()
