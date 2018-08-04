# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?

# approach 1: stack. Find the lower bound of the following number. Space: O(n)
# when the number begin to rise up, then the following number must be larger than the largest number which is smaller than the current number.
# use a stack to store the previous traversed number
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        lower_bound = float('-inf')
        for num in preorder:
            if num <= lower_bound:
                return False
            while stack and num > stack[-1]:
                lower_bound = stack.pop()
            stack.append(num)
        return True


# approach 2: stack. But use preorder as the stack. Space: O(1)
# use a number to indicate the top of the stack. Monitor the assembly
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        top = -1
        lower_bound = float('-inf')
        for num in preorder:
            if num <= lower_bound:
                return False
            while top >= 0 and num > preorder[top]:
                lower_bound = preorder[top]
                top -= 1
            top += 1
            preorder[top] = num
        return True
