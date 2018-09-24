# There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.
#
# You can keep inputting the password, the password will automatically be matched against the last n digits entered.
#
# For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.
#
# Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.
#
# Example 1:
# Input: n = 1, k = 2
# Output: "01"
# Note: "10" will be accepted too.
# Example 2:
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.
# Note:
# n will be in the range [1, 4].
# k will be in the range [1, 10].
# k^n will be at most 4096.

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = set()
        totalPossibility = pow(k, n)
        res = ['0' for _ in range(n)]
        visited.add(''.join(res))
        self.dfs(n, k, res, visited, totalPossibility)
        return ''.join(res)

    def dfs(self, n, k, res, visited, totalPossibility):
        if len(visited) == totalPossibility:
            return True
        prev = ''.join(res[len(res) - n + 1:])
        for i in range(k):
            curStr = prev + str(i)
            if curStr not in visited:
                visited.add(curStr)
                res.append(str(i))
                if self.dfs(n, k, res, visited, totalPossibility):
                    return True
                else:
                    visited.remove(curStr)
                    res.pop()
        return False
