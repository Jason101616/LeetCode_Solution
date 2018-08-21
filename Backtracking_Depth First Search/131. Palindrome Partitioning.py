# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


# idea: backtracking, find the possible substring and insert it into the ans and do the same process recursively until remain string is ''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        res = []
        self.find_parlin([], s, res)
        return res

    def find_parlin(self, prev_ans, remain_s, res):
        if remain_s == '':
            return res.append(prev_ans)
        for i in range(1, len(remain_s) + 1):
            if self.is_palindrome(remain_s[:i]):
                self.find_parlin(prev_ans + [remain_s[:i]], remain_s[i:], res)

    def is_palindrome(self, string):
        if not string:
            return True
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
