# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# For example:

# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# (1) whether there is no circle. use dfs
# (2) whether use all nodes. compare len(visited_nodes) with n in the end

from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.unvisited = set()
        self.visited = set()
        self.adj_list = defaultdict(lambda: [])
        self.find_adj()

    def find_adj(self):
        for edge in self.edges:
            self.unvisited.add(edge[0])
            self.unvisited.add(edge[1])
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.graph = Graph(edges)
        root = None
        for node in self.graph.unvisited:
            root = node
            break
        return self.dfs(root) and n == len(self.graph.visited)

    def dfs(self, node):
        self.graph.visited.add(node)
        # self.graph.unvisited.remove(node)
        for nod in self.graph.adj_list[node]:
            if nod in self.graph.visited:
                return False
            self.graph.adj_list[nod].remove(node)
            if not self.dfs(nod):
                return False
        return True
