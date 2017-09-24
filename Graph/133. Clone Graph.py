# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


# OJ's undirected graph serialization:
# Nodes are labeled uniquely.

# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.

# The graph has a total of three nodes, and therefore contains three parts as separated by #.

# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:

#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# DFS
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.visit={}
        
    def cloneGraph(self, node):
        if not node:
            return None
        if node.label in self.visit:
            return self.visit[node.label]
        self.visit[node.label] = UndirectedGraphNode(node.label)
        for new_node in node.neighbors:
            self.visit[node.label].neighbors.append(self.cloneGraph(new_node))
        return self.visit[node.label]
        
# BFS
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.visit = {}
        self.address = {}
        
    def cloneGraph(self, node):
        if not node:
            return None
        clone = UndirectedGraphNode(node.label)
        self.address[clone.label] = clone
        queue = deque()
        queue.append(node)
        while queue:
            current = queue.popleft()
            self.visit[current.label] = True
            if current.label in self.address:
                cur_clone = self.address[current.label]
            else:
                cur_clone = UndirectedGraphNode(current.label)
                self.address[current.label] = cur_clone
            append = False
            for n in current.neighbors:
                if n.label in self.address:
                    cur_clone.neighbors.append(self.address[n.label])
                else:
                    new_clone = UndirectedGraphNode(n.label)
                    self.address[new_clone.label] = new_clone
                    cur_clone.neighbors.append(new_clone)
                if n.label not in self.visit and not append:
                    queue.append(n)
                    append = True
        
        return clone
