# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Follow up:
# Could you solve it in O(nk) runtime?


# the same idea as 256 paint house. Maintain a dp array with the size n * k, where dp[i][j] means in the i th house, the minimum costs to paint the all the house until house i, and house i is painted with color j.
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        n = len(costs)
        k = len(costs[0])
        for i in range(1, n):
            for j in range(k):
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return min(costs[n - 1])
