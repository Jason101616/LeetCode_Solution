# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# Example 1:
#
# Input:  "69"
# Output: true
# Example 2:
#
# Input:  "88"
# Output: true
# Example 3:
#
# Input:  "962"
# Output: false

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapping = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}
        i = 0
        upperBound = len(num) // 2 if len(num) % 2 == 0 else len(num) // 2 + 1
        newNum = list(num)
        while i < upperBound:
            if num[i] not in mapping or num[len(num) - 1 - i] not in mapping:
                return False
            newNum[len(num) - 1 - i] = mapping[num[i]]
            newNum[i] == mapping[num[len(num) - 1 - i]]
            if newNum[i] != num[i] or newNum[len(num) - 1 - i] != num[len(num) - 1 - i]:
                return False
            i += 1
        return True