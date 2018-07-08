# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.
# choices = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

# Approach 1: Iterative Solution
# idea: maintain previous answer.
# When read a new number. First, find all the characters with that number, and store the number of numbers n corresponding to it.
# Then multiply the previous answer (n - 1) times. Just copy and paste.
# After that, add each section with one of the same new choices.
from copy import deepcopy
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ans = ['']
        choices = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        for digit in digits:
            cur_choice = choices[int(digit)]
            multiply = len(cur_choice)
            divisor = len(ans)
            tmp_ans = deepcopy(ans)
            for _ in range(multiply - 1):
                for i in tmp_ans:
                    ans.append(i)
            for i in range(len(ans)):
                ans[i] += cur_choice[i // divisor]
        
        return ans

# Approach 2: backtracking
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        self.choices = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.find_ans(digits, 0, res, '')
        return res
    
    def find_ans(self, digits, pos, res, cur_ans):
        if pos == len(digits):
            res.append(cur_ans)
            return
        
        for char in self.choices[int(digits[pos])]:
            self.find_ans(digits, pos + 1, res, cur_ans + char)           