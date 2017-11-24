# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

# idea: use dfs to perform topological sort
from collections import defaultdict


class Graph:
    def __init__(self, edges, num_nodes):
        self.edges = edges
        self.unvisited = set()
        self.visited = set()
        self.adj_list = defaultdict(lambda: [])
        for i in range(num_nodes):
            self.unvisited.add(i)
        # self.find_adj_undirected()
        self.find_adj_directed()

    def find_adj_undirected(self):
        for edge in self.edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])

    def find_adj_directed(self):
        for edge in self.edges:
            self.adj_list[edge[1]].append(edge[0])


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = Graph(prerequisites, numCourses)
        self.list = []
        self.visited = {}
        for course in self.graph.unvisited:
            if not self.dfs(course):
                return []
        return self.list[::-1]

    def dfs(self, node):
        if node not in self.visited:
            self.visited[node] = -1
        elif self.visited[node] == -1:
            return False
        else:
            return True
        for nod in self.graph.adj_list[node]:
            if not self.dfs(nod):
                return False
        self.visited[node] = 1
        self.list.append(node)
        return True