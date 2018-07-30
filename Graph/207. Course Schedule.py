# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


# approach 1: dfs
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        visit = {}  # -1: visiting now, 1: have visited
        for item in prerequisites:
            in_deg = item[0]
            out_deg = item[1]
            if out_deg not in graph:
                graph[out_deg] = [in_deg]
            else:
                graph[out_deg].append(in_deg)

        for node in graph.keys():
            if not self.DFS(node, graph, visit):
                return False

        return True

    def DFS(self, node, graph, visit):
        if node not in visit:
            visit[node] = -1
        else:
            if visit[node] == -1:
                return False
            elif visit[node] == 1:
                return True

        for i in graph[node]:
            if i not in graph:
                continue
            if not self.DFS(i, graph, visit):
                return False

        visit[node] = 1
        return True

# approach 2: topological sort/BFS
from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = defaultdict(lambda: [])
        inDegree = defaultdict(lambda: 0)
        for prerequisite in prerequisites:
            edges[prerequisite[1]].append(prerequisite[0]) # store the outbound
            inDegree[prerequisite[0]] += 1
            inDegree[prerequisite[1]] += 0
        
        # Use a queue to do BFS
        q = deque()
        cnt = 0
        for course in inDegree:
            if inDegree[course] == 0:
                q.append(course)
                cnt += 1
        while q:
            curCourse = q.popleft()
            for course in edges[curCourse]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    q.append(course)
                    cnt += 1
        return cnt == len(inDegree)