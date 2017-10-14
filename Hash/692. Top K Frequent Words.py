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
# idea: simply use priority queue

import queue
class Word:
    def __init__(self, word):
        self.word = word
        self.freq = 1
    
    def __lt__(self, other):
        # words with low frequency and high alphabetical order have high priority, as we need to delete them
        return (self.freq, other.word) < (other.freq, self.word)


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_dict = {}
        word_queue = queue.PriorityQueue()
        for word in words:
            if word not in word_dict:
                word_dict[word] = Word(word)
            else:
                word_dict[word].freq += 1
        for word in word_dict.keys():
            word_queue.put(word_dict[word])
            if word_queue.qsize() > k:
                word_queue.get()
        ret_list = [None] * k
        # reverse the priority queue, as we need the word with highest frequency first
        for i in range(k):
            ret_list[k - 1 - i] = word_queue.get().word
        return ret_list
        
        