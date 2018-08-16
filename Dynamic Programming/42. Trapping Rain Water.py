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
        maxLeft = [0 for _ in range(len(height))]
        maxRight = list(maxLeft)

        maxLeft[0] = height[0]
        for i in range(1, len(height) - 1):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        maxRight[len(height) - 1] = height[-1]
        for i in range(len(height) - 2, 0, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        res = 0
        for i in range(1, len(height) - 1):
            res += min(maxLeft[i], maxRight[i]) - height[i]
        return res
