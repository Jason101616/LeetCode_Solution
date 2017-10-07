# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

# Time:  O(n^n)
# Space: O(n)
# idea: naive implementation. Just use recursion. Time Limit Exceeded. 
# the recursion formula is: WB(S, Dict, start_index)
# WB(S, Dict, 0) = (1<= i <= n) WB(i) && s[0:i] in Dict 
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        return self.recursion_wordBreak(s, wordSet, 0)
        
    def recursion_wordBreak(self, s, wordSet, s_index):
        if s_index == len(s):
            return True
        
        for e_index in range(s_index + 1, len(s) + 1):
            if s[s_index: e_index] in wordSet and self.recursion_wordBreak(s, wordSet, e_index):
                return True
        
        return False

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
        memo = [None for i in range(len(s))]
        return self.recursion_wordBreak(s, wordSet, 0, memo)
        
    def recursion_wordBreak(self, s, wordSet, s_index, memo):
        if s_index == len(s):
            return True
        if memo[s_index] != None:
            return memo[s_index]
        
        for e_index in range(s_index + 1, len(s) + 1):
            if s[s_index: e_index] in wordSet and self.recursion_wordBreak(s, wordSet, e_index, memo):
                memo[s_index] = True
                return True
        
        memo[s_index] = False
        return False

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
        