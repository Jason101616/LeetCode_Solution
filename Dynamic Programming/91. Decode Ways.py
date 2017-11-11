# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.


# idea: dp, very similar to 70 climbing stairs except that 一位数时不能为0，两位数不能大于26，其十位上的数也不能为0
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        len_s = len(s)
        if len_s == 1:
            return 1 if int(s) >= 1 and int(s) <= 26 else 0
        dp = [0 for i in range(len_s)]
        dp[0] = 1 if int(s[0]) >= 1 else 0

        tmp = 1 if int(s[0]) != 0 and int(s[:2]) <= 26 and int(
            s[:2]) >= 1 else 0
        if int(s[1]) == 0:
            dp[1] = tmp
        else:
            dp[1] = dp[0] + tmp

        for i in range(2, len_s):
            if dp[i - 1] == 0 and dp[i - 2] == 0:
                return 0
            if int(s[i]) == 0:
                dp[i] = dp[i - 2] if int(s[i - 1]) != 0 and int(
                    s[i - 1:i + 1]) >= 1 and int(s[i - 1:i + 1]) <= 26 else 0
            else:
                dp[i] = dp[i - 1] if int(s[i - 1:i + 1]) > 26 or int(
                    s[i - 1]) == 0 else dp[i - 1] + dp[i - 2]
        return dp[len_s - 1]