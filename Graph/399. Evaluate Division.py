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
# (2) use dfs to find the answer, now the edge should contain the weights
# time complexity: O(N + E), where N is the number of nodes, E is the number of edges in the graph
from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.graph = defaultdict(lambda: [])
        len_equ = len(equations)
        for i in range(len_equ):
            node0, node1, val = equations[i][0], equations[i][1], values[i]
            self.graph[node0].append([node1, val])
            self.graph[node1].append([node0, 1 / val])
        len_qu = len(queries)
        self.ans = [-1 for _ in range(len_qu)]
        for i in range(len_qu):
            self.visited = set()
            self.find_ans = False
            self.cal_equ([], queries[i][0], queries[i][1], i)
        return self.ans

    def cal_equ(self, prev_route, cur_node, target, index):
        if cur_node not in self.graph:
            self.find_ans = True
            return
        if self.find_ans:
            return
        if cur_node == target:
            # calculate the answer
            cal_sum = 1
            for node in prev_route:
                cal_sum *= node[1]
            self.ans[index] = cal_sum
            self.find_ans = True
            return
        self.visited.add(cur_node)
        for i in range(len(self.graph[cur_node])):
            if self.graph[cur_node][i][0] not in self.visited:
                self.cal_equ(prev_route + [self.graph[cur_node][i]],
                             self.graph[cur_node][i][0], target, index)
