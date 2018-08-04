# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# idea: use DFS, and use a variable to record how many component already visited.
# be careful to use copy to avoid the error of Set changed size during iteration
# also in the end add n - len(visited_node)
from collections import defaultdict
from copy import copy


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.unvisited = set()
        self.visited = set()
        self.adj_list = defaultdict(lambda: [])
        # self.find_adj_undirected()
        # self.find_adj_directed()

    def find_adj_undirected(self):
        for edge in self.edges:
            self.unvisited.add(edge[0])
            self.unvisited.add(edge[1])
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])

    def find_adj_directed(self):
        for edge in self.edges:
            self.unvisited.add(edge[0])
            self.unvisited.add(edge[1])
            self.adj_list[edge[1]].append(edge[0])


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.graph = Graph(edges)
        cnt = 0
        for node in copy(self.graph.unvisited):
            if node not in self.graph.visited:
                self.dfs(node)
                cnt += 1
        return cnt + n - len(self.graph.visited)

    def dfs(self, node):
        self.graph.visited.add(node)
        self.graph.unvisited.remove(node)
        for nod in self.graph.adj_list[node]:
            if nod not in self.graph.visited:
                self.dfs(nod)
