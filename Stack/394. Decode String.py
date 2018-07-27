# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        cnt = ''
        for char in s:
            if char.isdigit():
                cnt += char
            elif char == '[':
                stack.append(['', int(cnt)])
                cnt = ''
            elif char == ']':
                string, k = stack.pop()
                stack[-1][0] += string * k
            else:
                stack[-1][0] += char
        return stack[0][0]

# Solution 2: recursion
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.helper(s, 0, '')[0]

    def helper(self, s, idx, curRes):
        cnt = ''
        while idx < len(s):
            if s[idx].isdigit():
                cnt += s[idx]
                idx += 1
            elif s[idx] == '[':
                res, newIdx = self.helper(s, idx + 1, '')
                curRes += int(cnt) * res
                cnt = ''
                idx = newIdx
            elif s[idx] == ']':
                return curRes, idx + 1
            else:
                curRes += s[idx]
                idx += 1
        return curRes, idx
