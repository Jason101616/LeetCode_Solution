# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

# Example 1:
# Input: 12
# Output: 21
# Example 2:
# Input: 21
# Output: -1


# idea: very similar to next permutation, be careful about the 32-bit limitation
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return -1
        numsList = self.parseInt(n)
        pos = len(numsList)
        for i in range(len(numsList) - 2, -1, -1):
            if numsList[i] < numsList[i + 1]:
                pos = i
                break
        if pos == len(numsList):
            return -1
        # start from pos to right, find the pos2, which satisfy numsList[pos2] > numsList[pos] >= numsList[pos2+1]
        pos2 = len(numsList) - 1
        for i in range(pos + 1, len(numsList) - 1):
            if numsList[i] > numsList[pos] >= numsList[i + 1]:
                pos2 = i
                break
        # swap element in pos and pos2
        numsList[pos], numsList[pos2] = numsList[pos2], numsList[pos]
        # reverse the number start from pos+1
        numsList[pos + 1:] = sorted(numsList[pos + 1:])
        res = self.buildInt(numsList)
        return res if res < pow(2, 31) else -1

    def parseInt(self, n):
        res = []
        while n:
            res.append(n % 10)
            n /= 10
        return res[::-1]

    def buildInt(self, numsList):
        res = 0
        for i in range(len(numsList)):
            res *= 10
            res += numsList[i]
        return res
