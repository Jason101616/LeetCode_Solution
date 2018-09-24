# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
#
# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.
#
# Example:
# Input:
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation:
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Note:
#
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.

# BFS, visited store the point
from collections import defaultdict, deque


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        numAllStation = defaultdict(lambda: set())
        for routeIdx, route in enumerate(routes):
            for idx, station in enumerate(route):
                numAllStation[station].add(routeIdx)

        visited = set()
        q = deque([S])
        visited.add(S)
        cnt = 0
        while q:
            if T in visited:
                return cnt
            cnt += 1
            curLen = len(q)
            for i in range(curLen):
                curPoint = q.popleft()
                nextRouteIdxs = numAllStation[curPoint]
                for idx in nextRouteIdxs:
                    points = routes[idx]
                    for point in points:
                        if point not in visited:
                            q.append(point)
                            visited.add(point)
        return -1

# a much faster BFS, visited store the route
from collections import defaultdict, deque


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        numAllRoutes = defaultdict(lambda: set())
        for routeIdx, route in enumerate(routes):
            for idx, station in enumerate(route):
                numAllRoutes[station].add(routeIdx)

        visited = set()
        q = deque([S])
        cnt = 0
        while q:
            cnt += 1
            curLen = len(q)
            for i in range(curLen):
                curPoint = q.popleft()
                nextRouteIdxs = numAllRoutes[curPoint]
                for idx in nextRouteIdxs:
                    if idx not in visited:
                        visited.add(idx)
                        points = routes[idx]
                        for point in points:
                            if point == T:
                                return cnt
                            q.append(point)
        return -1