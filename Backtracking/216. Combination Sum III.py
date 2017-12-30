# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


# Example 1:

# Input: k = 3, n = 7

# Output:

# [[1,2,4]]

# Example 2:

# Input: k = 3, n = 9

# Output:

# [[1,2,6], [1,3,5], [2,3,4]]

# idea: backtracking.
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.find_combination(k, n, 0, [])
        return self.ans
    
    def find_combination(self, k, n, index, cur_ans):
        if len(cur_ans) == k:
            if sum(cur_ans) == n:
                self.ans.append(cur_ans)
            return
        if index == 9:
            return
        for i in range(index + 1, 10):
            self.find_combination(k, n, i, cur_ans + [i])