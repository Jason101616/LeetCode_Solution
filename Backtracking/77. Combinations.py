# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


# idea: similar as permutation, but you can't choose number which index is smaller than the current number
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        ans = []
        self.find_combine(ans, k, [], 1, n)
        return ans

    def find_combine(self, ans, k, cur, start, n):
        if len(cur) == k:
            ans.append(list(cur))
            return
        if start == n + 1:
            return
        for i in range(start, n + 1):
            cur.append(i)
            self.find_combine(ans, k, cur, i + 1, n)
            cur.pop()

# Approach 2: use itertools
import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(itertools.combinations(range(1, n+1), k))