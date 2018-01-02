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
            else:
                exit(2)

        for i in graph[node]:
            if i not in graph:
                continue
            if not self.DFS(i, graph, visit):
                return False

        visit[node] = 1
        return True

# approach 2: topological sort/BFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(lambda: [])
        in_degree = collections.defaultdict(lambda: 0)
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])  # store outbound
            in_degree[edge[0]] += 1         # count the number of inbound
            in_degree[edge[1]] += 0         # a trick to put every node in in_degree
        target = len(in_degree)
        q = collections.deque()
        cnt = 0
        for node in in_degree:
            if in_degree[node] == 0:
                cnt += 1
                q.append(node)
        
        while q:
            cur_node = q.popleft()
            for neighbor in graph[cur_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    cnt += 1
                    q.append(neighbor)
        return cnt == target