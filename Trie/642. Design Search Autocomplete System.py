# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
# Your job is to implement the following functions:

# The constructor function:

# AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

# Now, the user wants to input a new sentence. The following function will provide the next character the user types:

# List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.


# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2]) 
# The system have already tracked down the following sentences and their corresponding times: 
# "i love you" : 5 times 
# "island" : 3 times 
# "ironman" : 2 times 
# "i love leetcode" : 2 times 
# Now, the user begins another search: 

# Operation: input('i') 
# Output: ["i love you", "island","i love leetcode"] 
# Explanation: 
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored. 

# Operation: input(' ') 
# Output: ["i love you","i love leetcode"] 
# Explanation: 
# There are only two sentences that have prefix "i ". 

# Operation: input('a') 
# Output: [] 
# Explanation: 
# There are no sentences that have prefix "i a". 

# Operation: input('#') 
# Output: [] 
# Explanation: 
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search. 

# Note:
# The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
# The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
# Please use double-quote instead of single-quote when you write test cases even for a character input.
# Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.

# AutocompleteSystem() takes O(k*l) time. We need to iterate over l sentences each of average length k, to create the trie for the given set of sentencessentences.

# input() takes O(p+q+mlog(m)) time. Here, p refers to the length of the sentence formed till now
# q refers to the number of nodes in the trie considering the sentence formed till now as the root node. Again, we need to sort the list of length m indicating the options available for the hot sentences, which takes O(mlog(m)) time.
class TrieNode:
    def __init__(self, is_word=False):
        self.next = {}
        self.is_word = is_word
        self.times = 0


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word, times=1):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for char in word:
            if char not in cur_node.next:
                cur_node.next[char] = TrieNode()
            cur_node = cur_node.next[char]
        cur_node.is_word = True
        cur_node.times = times

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        end_node = self.find_node(word)
        if end_node and end_node.is_word:
            return True
        return False

    def find_words(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.next:
                return []
            cur_node = cur_node.next[char]
        ans = []
        if cur_node.is_word:
            ans.append(prefix)
        for key in cur_node.next.keys():
            self.dfs(prefix + key, cur_node.next[key], ans)
        return ans

    def dfs(self, prefix, cur_node, ans):
        if cur_node.is_word:
            ans.append(prefix)
        for key in cur_node.next.keys():
            self.dfs(prefix + key, cur_node.next[key], ans)

    def find_node(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.next:
                return None
            cur_node = cur_node.next[char]
        return cur_node


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        # insert the sentence into the trie
        self.trie = Trie()
        for i, sentence in enumerate(sentences):
            self.trie.insert(sentence, times[i])
        # maintain a string jot down the current sentence,
        # when encounter #, reset this variable
        self.cur_sentence = ''

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != '#':
            self.cur_sentence += c
            # acquire the candidates
            candidates = self.trie.find_words(self.cur_sentence)
            # acquire the times these candidate has shown up
            candidates_times = []
            for candidate in candidates:
                cur_node = self.trie.find_node(candidate)
                candidates_times.append([candidate, cur_node.times])
            # calculate the candidates we need to return
            candidates_times.sort(key=lambda x: (-x[1], x[0]))
            ret_sen = []
            for i in range(len(candidates_times)):
                ret_sen.append(candidates_times[i][0])
                if i == 2:
                    break
            return ret_sen

        else:
            # if current sentence in the trie, update times, and set is_word
            cur_node = self.trie.find_node(self.cur_sentence)
            if cur_node:
                cur_node.times += 1
                cur_node.is_word = True
            # else insert it into the trie
            else:
                self.trie.insert(self.cur_sentence)
            # reset current sentence variable
            self.cur_sentence = ''
            return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)