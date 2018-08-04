# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1:

# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3
# return [1]

# Example 2:

# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]

# Note:

# (1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

# (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# Solution 1: (TLE)
# idea:
# (1) construct the graph
# a set contains all the nodes, a set contains the visited nodes, a dict store the adjacent list of each node
# (2) calculate the height for each node, use dfs
# (3) sort the result of the height, return the node(s) with the minimum height
# time complexity is O(n ^ 2), for each node, I need to traverse the whole graph
from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.graph_edges = defaultdict(lambda: [])
        nodes = set()
        for i in range(n):
            nodes.add(i)
        for edge in edges:
            self.graph_edges[edge[0]].append(edge[1])
            self.graph_edges[edge[1]].append(edge[0])
        height = []
        for node in nodes:
            self.visited = set()
            height.append([node, self.cal_height(node)])
        height.sort(key=lambda x: x[1])
        ans = []
        for i in range(len(height)):
            if height[i][1] == height[0][1]:
                ans.append(height[i][0])
            else:
                break
        return ans

    def cal_height(self, cur_node):
        self.visited.add(cur_node)
        is_leaf = True
        height_list = []
        for node in self.graph_edges[cur_node]:
            if node not in self.visited:
                height_list.append(self.cal_height(node))
                is_leaf = False
        if is_leaf == True:
            return 1
        return max(height_list) + 1


# Solution 2:
# 类似于剥洋葱。我们开始将所有只有一个连接边的节点(叶节点)都存入到一个队列queue中，然后我们遍历每一个叶节点，通过图来找到和其相连的节点，并且在其相连节点的集合中将该叶节点删去，如果删完后此节点也也变成一个叶节点了，加入队列中，再下一轮删除。那么我们删到什么时候呢，当节点数小于等于2时候停止，此时剩下的一个或两个节点就是我们要求的最小高度树的根节点.
class Solution {
public:
    vector < int > findMinHeightTrees(int


n, vector < pair < int, int > > & edges) {
if (n == 1)
return {0};
vector < int > res;
vector < unordered_set < int >> adj(n);
queue < int > q;
for (auto edge: edges) {
    adj[edge.first].insert(edge.second);
adj[edge.second].insert(edge.first);
}
for (int i = 0; i < n; ++i) {
if (adj[i].size() == 1) q.push(i);
}
while (n > 2) {
int size = q.size();
n -= size;
for (int i = 0; i < size; ++i) {
int t = q.front(); q.pop();
for (auto a: adj[t]) {
    adj[a].erase(t);
if (adj[a].size() == 1)
q.push(a);
}
}
}
while (!q.empty()) {
res.push_back(q.front()); q.pop();
}
return res;
}
};
