# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

# Approach 1: Recursion with memo
# Time:  O(n^2)
# Space: O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {}
        res = self.helper(s, set(wordDict), 0, memo)
        return [' '.join(re) for re in res]

    def helper(self, s, wordDict, idx, memo):
        if idx in memo:
            return memo[idx]

        curRes = []
        for i in range(idx + 1, len(s) + 1):
            tmpStr = s[idx: i]
            if tmpStr in wordDict:
                if i == len(s):
                    curRes.append([tmpStr])
                else:
                    res = self.helper(s, wordDict, i, memo)
                    if res:
                        res = [[tmpStr] + r for r in res]
                        curRes.extend(res)
        memo[idx] = curRes
        return curRes


# Approach 2: bottom-up. TLE.
# Time:  O(n^2)
# Space: O(n)
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
