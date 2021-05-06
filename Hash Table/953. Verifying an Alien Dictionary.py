# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

# idea: ez
# Time: O(len(words) * average_words_length)
# space: O(1)

from collections import defaultdict


class Solution:
    def __init__(self):
        self.char_2_order = defaultdict(lambda x: 0)

    def is_sorted(self, str1, str2):
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if self.char_2_order[str1[i]] < self.char_2_order[str2[i]]:
                return True
            if self.char_2_order[str1[i]] > self.char_2_order[str2[i]]:
                return False
        if len(str1) > len(str2):
            return False
        return True

    def is_alien_sorted(self, words: list[str], order: str) -> bool:
        for idx, char in enumerate(order):
            self.char_2_order[char] = idx
        for i in range(len(words) - 1):
            if not self.is_sorted(words[i], words[i + 1]):
                return False
        return True
