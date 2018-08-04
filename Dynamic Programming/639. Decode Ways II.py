# A message containing letters from A-Z is being encoded to numbers using the following mapping way:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

# Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

# Also, since the answer may be very large, you should return the output mod 109 + 7.

# Example 1:
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
# Example 2:
# Input: "1*"
# Output: 9 + 9 = 18
# Note:
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.

# 建立一个一维dp数组，其中dp[i]表示前i个字符(从1开始)的解码方法等个数，长度为字符串的长度加1。将dp[0]初始化为1，然后我们判断，如果字符串第一个字符是0，那么直接返回0，如果是*，则dp[1]初始化为9，否则初始化为1。
# 下面就来计算一般情况下的dp[i]了，我们从i=2开始遍历，由于要分的情况种类太多，我们先选一个大分支，就是当前遍历到的字符s[i-1]，只有三种情况，要么是0，要么是1到9的数字，要么是星号。我们一个一个来分析：

# 首先来看s[i-1]为0的情况，这种情况相对来说比较简单，因为0不能单独拆开，只能跟前面的数字一起，而且前面的数字只能是1或2，其他的直接返回0即可。那么当前面的数字是1或2的时候，dp[i]的种类数就跟dp[i-2]相等，可以参见之前那道Decode Ways的讲解，因为后两数无法单独拆分开，就无法产生新的解码方法，所以只保持住原来的拆分数量就不错了；
# 如果前面的数是星号的时候，那么前面的数可以为1或者2，这样就相等于两倍的dp[i-2]；如果前面的数也为0，直接返回0即可。

# 再来看s[i-1]为1到9之间的数字的情况，首先搞清楚当前数字是可以单独拆分出来的，那么dp[i]至少是等于dp[i-1]的，不会拖后腿，还要看其能不能和前面的数字组成两位数进一步增加解码方法。那么就要分情况讨论前面一个数字的种类，如果当前数字可以跟前面的数字组成一个小于等于26的两位数的话，dp[i]还需要加上dp[i-2]；如果前面的数字为星号的话，那么要看当前的数字是否小于等于6，如果是小于等于6，那么前面的数字就可以是1或者2了，此时dp[i]需要加上两倍的dp[i-2]，如果大于6，那么前面的数字只能是1，所以dp[i]只能加上dp[i-2]。

# 最后来看s[i-1]为星号的情况，如果当前数字为星号，那么就创造9种可以单独拆分的方法，所以那么dp[i]至少是等于9倍的dp[i-1]，还要看其能不能和前面的数字组成两位数进一步增加解码方法。那么就要分情况讨论前面一个数字的种类，如果前面的数字是1，那么当前的9种情况都可以跟前面的数字组成两位数，所以dp[i]需要加上9倍的dp[i-2]；如果前面的数字是2，那么只有小于等于6的6种情况都可以跟前面的数字组成两位数，所以dp[i]需要加上6倍的dp[i-2]；如果前面的数字是星号，那么就是上面两种情况的总和，dp[i]需要加上15倍的dp[i-2]。

# 每次算完dp[i]别忘了对超大数取余

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        M = pow(10, 9) + 7
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 1

        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':  # i - 1 is the current index, dp[i] is the answer for index i - 1
                if s[i - 2] == '1' or s[i - 2] == '2':
                    dp[i] += dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += 2 * dp[i - 2]
                else:
                    return 0
            elif '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]
                if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                    dp[i] += dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += 2 * dp[i - 2] if s[i - 1] <= '6' else dp[i - 2]
            else:  # s[i - 1] == *
                dp[i] += 9 * dp[i - 1]
                if s[i - 2] == '1':
                    dp[i] += 9 * dp[i - 2]
                elif s[i - 2] == '2':
                    dp[i] += 6 * dp[i - 2]
                elif s[i - 2] == '*':
                    dp[i] += 15 * dp[i - 2]
            dp[i] %= M
        return dp[-1]
