# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

# Example 1:

# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# Example 3:

# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:

# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# Example 5:

# Input: num = "3456237490", target = 9191
# Output: []

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.findAns(num, target, res, 0, '', 0, 0)
        return res
    
    def findAns(self, num, target, res, idx, curPath, curAns, mulVal):
        if idx == len(num):
            if curAns == target:
                res.append(curPath)
            return
        
        for i in range(idx, len(num)):
            if i != idx and num[idx] == '0':
                break
            curNum = num[idx: i + 1]
            curVal = int(curNum)
            if idx == 0:
                self.findAns(num, target, res, i + 1, curPath + curNum, curVal, curVal)
            else:
                self.findAns(num, target, res, i + 1, curPath + '+' + curNum, curAns + curVal, curVal)
                self.findAns(num, target, res, i + 1, curPath + '-' + curNum, curAns - curVal, -curVal)
                self.findAns(num, target, res, i + 1, curPath + '*' + curNum, curAns - mulVal + mulVal * curVal, mulVal * curVal)
        