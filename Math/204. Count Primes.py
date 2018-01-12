# Description:

# Count the number of prime numbers less than a non-negative number, n.

# Approach 1: for each number, check whether it is a prime number
# we only need to check 2 through sqrt(n)

# TLE

# Approach 2: mark the non-prime number
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [False for _ in range(n)]
        cnt = 0
        for i in range(2, n):
            if not memo[i]:
                cnt += 1
                j = 2
                while j * i < n:
                    memo[j * i] = True
                    j += 1
        return cnt