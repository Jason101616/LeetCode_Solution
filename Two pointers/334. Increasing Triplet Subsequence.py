# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.

# use two pointer
# The main idea is keep two values when check all elements in the array: the minimum value min until now and the second minimum value secondMin from the minimum value's position until now. Then if we can find the third one that larger than those two values at the same time, it must exists the triplet subsequence and return true.
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = sec_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= sec_smallest:
                sec_smallest = num
            else:
                return True
        return False
                