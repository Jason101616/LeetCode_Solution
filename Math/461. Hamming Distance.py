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

def hammingDistance2(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x ^ y).count('1')

# Go version:
func hammingDistance(x int, y int) int {
	tmp := x ^ y
	res := 0
	for ;tmp != 0; {
		res += 1
		tmp = tmp &(tmp - 1)
	}
	return res
}