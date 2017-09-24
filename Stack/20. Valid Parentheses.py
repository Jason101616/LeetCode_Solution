# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 思路：
        # if char is left symbol, push into the stack
        # if char is right symbol. validate whether the top of the stack is its corresponding left symbol
        # in the end, the stack must be empty
        stack = []
        dict_symbol = {']': '[', '}':'{', ')':'('}
        for char in s:
            if char in dict_symbol.values():
                stack.append(char)
            else:
                if stack == [] or stack.pop() != dict_symbol[char]:
                    return False
        return stack == []
    