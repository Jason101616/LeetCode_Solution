# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5
# Note:
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        prevSign = '+'
        num = 0
        for idx, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() and char != ' ' or idx == len(s) - 1:
                if prevSign == '+':
                    stack.append(num)
                elif prevSign == '-':
                    stack.append(-num)
                elif prevSign == '*':
                    stack.append(num * stack.pop())
                elif prevSign == '/':
                    stack.append(int(float(stack.pop()) / num))
                prevSign = char
                num = 0
        return sum(stack)
