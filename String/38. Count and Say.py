# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

# Example 1:

# Input: 1
# Output: "1"
# Example 2:

# Input: 4
# Output: "1211"

# 思路：记录连续出现的char的次数以及char本身，每次都添加到一个list中，最后再join即可
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = "1"
        for i in range(n - 1):
            cur = self.nextOne(cur)

        return cur

    def nextOne(self, cur):
        res = []
        tmp = cur[0]
        prev = 0
        for i in range(prev + 1, len(cur)):
            if cur[i] != tmp:
                res.append(str(i - prev))
                res.append(tmp)
                prev = i
                tmp = cur[i]
        res.append(str(len(cur) - prev))
        res.append(tmp)
        return ''.join(res)
