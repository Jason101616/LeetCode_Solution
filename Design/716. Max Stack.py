# Design a max stack that supports push, pop, top, peekMax and popMax.

# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
# Example 1:
# MaxStack stack = new MaxStack();
# stack.push(5); 
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# Note:
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.

# approach 1: use 2 stacks
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # store the current max element in the stack
        self.max_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        # find whether x is the largest element in the stack. 
        # If not push the same element of the top of the max_stack into max_stack
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            if x > self.max_stack[-1]:
                self.max_stack.append(x)
            else:
                self.max_stack.append(self.max_stack[-1])

    def pop(self):
        """
        :rtype: int
        """
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        cur_max = self.max_stack[-1]
        # pop the element in stack if it is not equal to cur_max
        # put the temp element in a new stack, and then push it back to the stack
        tmp_stack = []
        while self.stack[-1] != cur_max:
            tmp_stack.append(self.pop())
        self.pop()
        while tmp_stack:
            self.push(tmp_stack.pop())
        return cur_max

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
