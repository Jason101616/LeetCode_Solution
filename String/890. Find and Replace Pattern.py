# You have a list of words and a pattern, and you want to know which words in words matches the pattern.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

# Return a list of the words in words that match the given pattern. 

# You may return the answer in any order.

 

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.
 

# Note:

# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.helper(word, pattern):
               res.append(word)
        return res
    
    def helper(self, word, pattern):
        if len(word) != len(pattern):
            return False
        mapping = {}
        used = set()
        for i in range(len(word)):
            if word[i] not in mapping:
                if pattern[i] in used:
                    return False
                mapping[word[i]] = pattern[i]
                used.add(pattern[i])
            else:
                if mapping[word[i]] != pattern[i]:
                    return False
        return True
        