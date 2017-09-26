# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 思路：一个一个位置比较即可
        if s == "":
            return True
        
        self.letters = string.ascii_letters + string.digits
        i = self.next_char_pos(s, 0)
        j = self.prev_char_pos(s, len(s) - 1)
        while i < j:
            if s[i].upper() != s[j].upper():
                return False
            i = self.next_char_pos(s, i + 1)
            j = self.prev_char_pos(s, j - 1)
        
        return True
    
    def next_char_pos(self, s, index):
        while s[index] not in self.letters:
            index += 1
            if index == len(s):
                return index
        return index
    
    def prev_char_pos(self, s, index):
        while s[index] not in self.letters:
            index -= 1
            if index == -1:
                return index
        return index
                          

# 精简思路版本
import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        
        return True
                          