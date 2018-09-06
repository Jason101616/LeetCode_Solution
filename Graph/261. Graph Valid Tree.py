# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
#

# (1) whether there is no circle. BFS or DFS
# (2) whether use all nodes. compare cnt with n in the end

from collections import defaultdict, deque


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges:
            return n == 1
        graphEdges = defaultdict(lambda: set())

        for edge in edges:
            startNode, nextNode = edge
            graphEdges[startNode].add(nextNode)
            graphEdges[nextNode].add(startNode)

        q = deque([startNode])
        visited = set([startNode])
        cnt = 1
        while q:
            curNode = q.popleft()
            for nextNode in graphEdges[curNode].copy():
                if nextNode in visited:
                    return False
                q.append(nextNode)
                visited.add(nextNode)
                graphEdges[curNode].remove(nextNode)
                graphEdges[nextNode].remove(curNode)
                cnt += 1
        return cnt == n