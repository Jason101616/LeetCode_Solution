# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group. 

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.

 

# Example 1:

# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:

# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:

# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
 

# Note:

# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].

# idea: for each connected graph, color each node, there shouldn't be any conflicts.
# The rules are that any neighbor node should have different color

from collections import defaultdict


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if not dislikes:
            return True
        graph = defaultdict(lambda: [])
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        visited = {}
        for node in graph:
            if node not in visited:
                if not self.dfs(node, 1, visited, graph):
                    return False
        return True

    def dfs(self, node, color, visited, graph):
        if node in visited:
            return visited[node] == color
        visited[node] = color
        for neighbor in graph[node]:
            if not self.dfs(neighbor, -color, visited, graph):
                return False
        return True

