# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


# Time:  O(n^2)
# Space: O(n)
# idea: bottom-up method. LTE don't know why.
import copy
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        memo = [[False, []] for _ in range(len(s) + 1)]
        memo[0][0] = True
        memo[0][1] = [[]]
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if memo[j][0] and s[j: i] in wordSet:
                    # update the answer of memo[j][1]
                    tmp = copy.deepcopy(memo[j][1])
                    for k in tmp:
                        k.append(s[j: i])
                    memo[i][1].extend(tmp)
                    memo[i][0] = True

        ret = memo[len(s)][1]
        for i in range(len(ret)):
            ret[i] = ' '.join(ret[i])
        return ret
                    
        