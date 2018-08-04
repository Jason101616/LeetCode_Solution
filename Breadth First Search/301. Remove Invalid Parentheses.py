# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]

# idea: BFS
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.visited = set()
        queue = deque()
        self.visited.add(s)
        queue.append(s)
        found = False
        while queue:
            current = queue.popleft()
            if self.is_valid(current):
                self.res.append(current)
                found = True
            if found:
                continue
            for index, char in enumerate(current):
                if char != '(' and char != ')':
                    continue
                new_str = current[:index] + current[index + 1:]
                if new_str not in self.visited:
                    self.visited.add(new_str)
                    queue.append(new_str)
        return self.res

    def is_valid(self, s):
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            elif char == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0
