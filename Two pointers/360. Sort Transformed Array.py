# Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example 1:
#
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# Example 2:
#
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        res = list(nums)
        l, r = 0, len(nums) - 1
        idx = r if a > 0 else l
        while l <= r:
            lRes, rRes = self.helper(nums[l], a, b, c), self.helper(nums[r], a, b, c)
            if a > 0:
                if lRes > rRes:
                    res[idx] = lRes
                    l += 1
                else:
                    res[idx] = rRes
                    r -= 1
                idx -= 1
            else:
                if lRes > rRes:
                    res[idx] = rRes
                    r -= 1
                else:
                    res[idx] = lRes
                    l += 1
                idx += 1
        return res

    def helper(self, x, a, b, c):
        return a * x * x + b * x + c