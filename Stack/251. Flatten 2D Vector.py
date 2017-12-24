# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.

# same idea as 341. Flatten Nested List Iterator. Use a stack.
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.stack = list()
        for vec in vec2d[::-1]:
            self.stack.append(vec)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if not isinstance(self.stack[-1], list):
                return True
            for num in self.stack.pop()[::-1]:
                self.stack.append(num)
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())