# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

# Approach 1: recursion. Time Limit Exceeded.
# Time:  O(2^n)
# Space: O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        return self.helper(s, 0, wordSet)

    def helper(self, s, idx, wordSet):
        if idx == len(s):
            return True
        for i in range(idx + 1, len(s) + 1):
            if s[idx: i] in wordSet:
                if self.helper(s, i, wordSet):
                    return True
        return False


# Approach 2:
# Time:  O(n^2)
# Space: O(n)
# idea: Recursion with memo. Top-down with memorization.
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        memo = {}
        return self.helper(s, 0, wordSet, memo)

    def helper(self, s, idx, wordSet, memo):
        if idx in memo:
            return memo[idx]
        if idx == len(s):
            return True
        for i in range(idx + 1, len(s) + 1):
            if s[idx: i] in wordSet:
                if self.helper(s, i, wordSet, memo):
                    memo[idx] = True
                    return True
        memo[idx] = False
        return False


# Approach 3:
# Time:  O(n^2)
# Space: O(n)
# idea: bottom-up method. Nearly the same time with the previous method.
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        memo = [False for i in range(len(s) + 1)]
        memo[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if memo[j] and s[j: i] in wordSet:
                    memo[i] = True
                    break

        return memo[len(s)]
