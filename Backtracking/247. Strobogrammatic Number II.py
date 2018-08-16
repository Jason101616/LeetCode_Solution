# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
# Input:  n = 2
# Output: ["11","69","88","96"]

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)

    def helper(self, n, m):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        prevRes = self.helper(n - 2, m)
        res = []
        for prev in prevRes:
            if n != m:
                res.append('0' + prev + '0')
            res.append('1' + prev + '1')
            res.append('6' + prev + '9')
            res.append('8' + prev + '8')
            res.append('9' + prev + '6')
        return res