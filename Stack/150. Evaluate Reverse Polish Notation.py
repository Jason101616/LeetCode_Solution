# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = ['+', '-', '*', '/']
        op_set = set(operations)
        stack = []
        for token in tokens:
            if token not in op_set:
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '+':
                    cur_res = op1 + op2
                elif token == '-':
                    cur_res = op2 - op1
                elif token == '*':
                    cur_res = op1 * op2
                else:
                    cur_res = int(op2 / op1)
                stack.append(cur_res)
        return stack[0]
