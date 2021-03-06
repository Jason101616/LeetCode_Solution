# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".

# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# idea: use 2 dict to count
# brute force:
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def isSubset(cntT, cntS):
            for char in cntT:
                if char not in cntS or cntS[char] < cntT[char]:
                    return False
            return True

        cntT = {}
        for char in t:
            if char not in cntT:
                cntT[char] = 0
            cntT[char] += 1

        l, res, minLen = 0, '', len(s) + 1
        cntS = {}
        for idx, char in enumerate(s):
            if char in cntT:
                if char not in cntS:
                    cntS[char] = 0
                cntS[char] += 1
                if isSubset(cntT, cntS):
                    while isSubset(cntT, cntS):
                        if idx - l + 1 < minLen:
                            minLen = idx - l + 1
                            res = s[l: idx + 1]
                        if s[l] in cntS:
                            cntS[s[l]] -= 1
                            if cntS[s[l]] == 0:
                                del cntS[s[l]]
                        l += 1
        return res

# better implementation
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt_t = collections.defaultdict(lambda: 0)
        for char in t:
            cnt_t[char] += 1
        res_len = float('inf')
        res = ''
        left = 0
        cnt = len(t)

        for index, char in enumerate(s):
            if char in cnt_t:
                if cnt_t[char] > 0:
                    cnt -= 1
                cnt_t[char] -= 1
                while cnt == 0:
                    # compute the answer and make it invalid
                    if index - left + 1 < res_len:
                        res_len = index - left + 1
                        res = s[left: index + 1]
                    if s[left] in cnt_t:
                        if cnt_t[s[left]] == 0:
                            cnt += 1
                        cnt_t[s[left]] += 1
                    left += 1
        return res
