# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?

# Stack solution
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.helper(S) == self.helper(T)

    def helper(self, s):
        stack = []
        for char in s:
            if char != '#':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return stack

# Real O(1) Solution:
# class Solution {
#     public boolean backspaceCompare(String S, String T) {
#         int i = S.length() - 1;
#         int j = T.length() - 1;
#         int skipi = 0;
#         int skipj = 0;
#
#         while (i >= 0 || j >= 0) {
#             while (i >= 0) {
#                 if (S.charAt(i) == '#') {
#                     skipi++;
#                     i--;
#                 } else if (skipi > 0) {
#                     i--;
#                     skipi--;
#                 } else {
#                     break;
#                 }
#             }
#
#             while (j >= 0) {
#                 if (T.charAt(j) == '#') {
#                     skipj++;
#                     j--;
#                 } else if (skipj > 0) {
#                     j--;
#                     skipj--;
#                 } else {
#                     break;
#                 }
#             }
#
#             if (i >= 0 && j >= 0 && S.charAt(i) != T.charAt(j)) {
#                 return false;
#             }
#             if ((i >= 0) != (j >= 0)) {
#                 // ex: S = "bxj##tw"; T = "bxj###tw";  i becomes 0 and j becomes -1
#                 return false;
#             }
#             i--;
#             j--;
#         }
#         return true;
#     }
# }