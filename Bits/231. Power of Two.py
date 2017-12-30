# Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and ((n & (n-1)) == 0)
    
    def isPowerOfTwo(self, n): 
        if n==0:
            return False
        while(n % 2 == 0):
            n /= 2;
        return n == 1;