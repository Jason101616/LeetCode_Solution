# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 2^31.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

# 思路：转换成二进制。数有几个数不同。注意一点是string左边是低位，所以比较时需要先将string倒置一下
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = 0
        x_str = bin(x)[2:]
        y_str = bin(y)[2:]
        if len(x_str) > len(y_str):
            tmp = x_str
            x_str = y_str
            y_str = tmp
        
        small_len = len(x_str)
        x_str = x_str[::-1]
        y_str = y_str[::-1]
        for i in range(small_len):
            if x_str[i] != y_str[i]:
                ret += 1
        
        for num in y_str[small_len:]:
            if num == '1':
                ret += 1
        
        return ret

# 进阶版：
def hammingDistance2(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x ^ y).count('1')