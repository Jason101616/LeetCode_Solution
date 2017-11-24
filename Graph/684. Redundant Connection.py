# In this problem, a tree is an undirected graph that is connected and has no cycles.

# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.


# idea: use union find.
# we simply find the first edge occurring in the graph that is already connected.
# time complexity: O(N), space complexity: O(N), where N is the number of nodes in the graph
class DSU(object):
    def __init__(self):
        self.par = range(1001)

    def find(self, x):
        # Path compression
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    # # without path compression
    # def find(self, x):
    #     while self.par[x] != x:
    #         x = self.par[x]
    #     return x

    def union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return False
        self.par[par_y] = par_x
        return True


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU()
        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return edge