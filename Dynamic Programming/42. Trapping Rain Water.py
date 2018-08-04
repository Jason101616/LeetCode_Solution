# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# intuition: the volume of water a point a trap equals to min(max_left, max_right) - height of current point
# first use dp to calculate the max_left and max_right of each point
# then calculate the volume of water each point can trap, and add up these volume
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        max_left = [0 for _ in range(len(height))]
        max_right = list(max_left)

        max_left[0] = height[0]
        for i in range(1, len(height) - 1):
            max_left[i] = max(max_left[i - 1], height[i])

        max_right[len(height) - 1] = height[-1]
        for i in range(len(height) - 2, 0, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        res = 0
        for i in range(1, len(height) - 1):
            res += min(max_left[i], max_right[i]) - height[i]
        return res
