# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# You may assume that the given expression is always valid.

# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        prev_sign = '+'
        for index, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() and char != ' ' or index == len(s) - 1:
                if prev_sign == '+':
                    stack.append(num)
                elif prev_sign == '-':
                    stack.append(-num)
                elif prev_sign == '*':
                    stack.append(stack.pop() * num)
                elif prev_sign == '/':
                    stack.append(int(float(stack.pop()) / num))
                prev_sign = char
                num = 0
        res = 0
        for num in stack:
            res += num
        return res
