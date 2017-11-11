# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        len_digit = len(digits)
        ret = [0 for _ in range(len_digit)]
        add_next = 1
        for i in range(len_digit - 1, -1, -1):
            cur_ans = digits[i] + add_next
            if cur_ans >= 10:
                cur_ans -= 10
                add_next = 1
            else:
                add_next = 0
            ret[i] = cur_ans
        if add_next:
            new_ret = [0 for _ in range(len_digit + 1)]
            new_ret[0] = 1
            new_ret[1:] = ret
            return new_ret
        else:
            return ret
