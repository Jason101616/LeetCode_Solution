# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.

from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.route = ["JFK"]
        self.graph = defaultdict(list)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        for ticket in tickets:
            depart = ticket[0]
            dest = ticket[1]
            self.graph[depart].append(dest)

        for key in self.graph.keys():
            self.graph[key].sort()
        self.length = len(tickets)
        return self.DFS("JFK")

    def DFS(self, depart):
        if len(self.route) == self.length + 1:
            return self.route
        tmp = sorted(self.graph[depart])
        for dest in tmp:
            self.graph[depart].remove(dest)
            self.route.append(dest)
            if self.DFS(dest):
                return self.route
            self.route.pop()
            self.graph[depart].append(dest)
        return []
