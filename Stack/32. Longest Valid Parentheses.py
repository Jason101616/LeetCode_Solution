# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# idea: use a stack. Careful about the edge case
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        stack = []
        left = 0
        for index, par in enumerate(s):
            if par == '(':
                stack.append(index)
            else:
                if stack:
                    stack.pop()
                    if not stack:
                        longest = max(longest, index - left + 1)
                    else:
                        longest = max(longest, index - stack[-1])  # still has element in the stack when traverse over
                else:
                    stack = []
                    left = index + 1
        return longest
