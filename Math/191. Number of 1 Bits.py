# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.


# trick: for any number nn, doing a bit-wise AND of n and n - 1 flips the least-significant 1-bit in n to 0.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n != 0:
            n &= (n - 1)
            cnt += 1
        return cnt

# solution2: hard code
class Solution(object):
    def __init__(self):
        self.mapping = {'0': 0, '1': 1, '2': 1, '3': 2, '4': 1, '5': 2, '6': 2, '7': 3, '8': 1,
                        '9': 2, 'a': 2, 'b': 3, 'c': 2, 'd': 3, 'e': 3, 'f': 4}

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hexRepre = hex(n)
        res = 0
        for i in range(2, len(hexRepre)):
            res += self.mapping[hexRepre[i]]
        return res
