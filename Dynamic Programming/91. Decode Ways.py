bv# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.


# idea: dp, very similar to 70 climbing stairs
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            # calculate the new dp index when only use current character
            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
            # update the new dp index when try to use previous character
            if s[i - 2] == '1' or s[i - 2] == '2' and s[i - 1] <= '6':
                dp[i] += dp[i - 2]
        return dp[-1]
