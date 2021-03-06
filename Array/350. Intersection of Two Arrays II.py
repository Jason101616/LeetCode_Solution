# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        retList = []
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        for key in cnt1:
            if key in cnt2:
                num = min(cnt1[key], cnt2[key])
                tmp = [key] * num
                retList.extend(tmp)

        return retList

# sort version
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        ptr1 = ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums2[ptr2] < nums1[ptr1]:
                ptr2 += 1
            else:
                res.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
        return res
