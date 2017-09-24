# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# rubbish question!!!

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char2int = {'I': 1, 'V' : 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        index = len(s) - 1
        prev = 0
        result = 0
        
        for i in range(index, -1, -1):
            tmp = char2int[s[i]]
            if tmp >= prev:
                result += tmp
            else:
                result -= tmp
            prev = tmp
            
        return result
    