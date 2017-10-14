# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

# Note:

# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
# Example 1:

# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]

# return: 1
# Example 2:

# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

# return: 2
# Example 3:

# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

# return: 3
# Time:  O(8 * n^3) n is the length of the bank, 8 is the length of the gene. (not sure this time complexity is correct)
# Space: O(n)
# idea: Sort the node and perform BFS from start node to end node. Add up the path.
import collections
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        visited = set()
        bank_set = set(bank)
        queue = collections.deque()
        visited.add(start)
        queue.append(start)
        cnt = -1
        while queue:
            cnt += 1
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                if current == end:
                    return cnt
                for gene in self.possible_mutation(current, bank):
                    if gene not in visited:
                        visited.add(gene)
                        queue.append(gene)

        return -1
    
    def possible_mutation(self, current, bank):
        poss_mut = []
        for gene in bank:
            diff = 0
            for i in range(8):
                if current[i] != gene[i]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                poss_mut.append(gene)
                
        return poss_mut
        