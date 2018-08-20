# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

# idea
# (1) construct the graph
# (2) dfs find the answer
# time complexity: O(len(queries) * (N + E)), where N is the number of nodes, E is the number of edges in the graph
from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(lambda: [])
        for i in range(len(equations)):
            node0, node1, val = equations[i][0], equations[i][1], values[i]
            graph[node0].append([node1, val])
            graph[node1].append([node0, 1 / val])
        res = [None for _ in range(len(queries))]
        for i in range(len(queries)):
            res[i] = self.helper(queries[i][0], queries[i][1], graph, {queries[i][0]})
        return res

    def helper(self, curNode, target, graph, visited):
        if curNode not in graph:
            return -1.0
        if curNode == target:
            return 1.0
        nextNodes = graph[curNode]
        for node in nextNodes:
            if node[0] not in visited:
                visited.add(node[0])
                tmpRes = self.helper(node[0], target, graph, visited)
                if tmpRes != -1.0:
                    return node[1] * tmpRes
                visited.remove(node[0])
        return -1.0
