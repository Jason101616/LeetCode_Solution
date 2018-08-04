# Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3
# Note:

# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].

# idea: compare one by one, whether that string is not the substring of all other string in strs
# return the longest length of the string


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_len = -1
        for i, cur_str in enumerate(strs):
            not_ans = False
            tmp_strs = strs[:i] + strs[(i + 1):]
            for tmp_str in tmp_strs:
                if self.is_subsequence(cur_str, tmp_str):
                    not_ans = True
                    break
            if not_ans:
                continue
            max_len = max(max_len, len(cur_str))
        return max_len

    def is_subsequence(self, A, B):
        j = 0
        for i in range(len(B)):
            if A[j] == B[i]:
                j += 1
            if j == len(A):
                return True
        return False
