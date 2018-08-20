# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
# Can you solve it in O(n) time with only O(k) extra space?

# time: O(n log k)
# space: O(n)
# idea: priority queue

from Queue import PriorityQueue


class Word:
    def __init__(self, word):
        self.word = word
        self.freq = 1

    def __lt__(self, other):
        # words with low frequency and high alphabetical order have high priority
        return (self.freq, other.word) < (other.freq, self.word)


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        mapping = {}
        for word in words:
            if word not in mapping:
                mapping[word] = Word(word)
            else:
                mapping[word].freq += 1
        pq = PriorityQueue()
        for word in mapping:
            pq.put(mapping[word])
            if pq.qsize() > k:
                pq.get()
        res = [None for _ in range(k)]
        for i in range(k - 1, -1, -1):
            res[i] = pq.get().word
        return res
