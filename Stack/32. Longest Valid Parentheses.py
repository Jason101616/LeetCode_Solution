# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

# idea: use a stack. Careful about the edge case
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastValidIdx, stack, res = 0, [], 0
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            else:   # char == ')'
                if stack:
                    stack.pop()
                    if stack:
                        res = max(res, idx - stack[-1])
                    else:
                        res = max(res, idx - lastValidIdx + 1)
                else:
                    lastValidIdx = idx + 1
        return res
