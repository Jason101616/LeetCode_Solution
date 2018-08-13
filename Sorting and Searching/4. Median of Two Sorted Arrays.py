# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

# Approach 1: merge sort
# time: O(m + n)
# space: O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        total = m + n
        if total % 2 != 0:
            return self.find_kth_num(nums1, nums2, total // 2 + 1)
        else:
            return (self.find_kth_num(nums1, nums2, total // 2) + self.find_kth_num(nums1, nums2, total // 2 + 1)) / 2.0

    def find_kth_num(self, nums1, nums2, k):
        i1 = i2 = cnt = 0
        while i1 < len(nums1) and i2 < len(nums2):
            cnt += 1
            if nums1[i1] < nums2[i2]:
                if cnt == k:
                    return nums1[i1]
                i1 += 1
            else:
                if cnt == k:
                    return nums2[i2]
                i2 += 1
        if i1 == len(nums1):
            return nums2[i2 + k - cnt - 1]
        else:
            return nums1[i1 + k - cnt - 1]


# Approach 2: binary search
# time: O(log(m + n))
# space: O(log(m + n))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2 != 0:
            return self.findKthNum(nums1, m, nums2, n, total // 2 + 1)
        else:
            return (self.findKthNum(nums1, m, nums2, n, total // 2) + self.findKthNum(nums1, m, nums2, n,
                                                                                      total // 2 + 1)) / 2.0

    def findKthNum(self, nums1, m, nums2, n, k):
        if m > n:
            return self.findKthNum(nums2, n, nums1, m, k)
        if m == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        i1 = min(k // 2, m)  # key point
        i2 = k - i1
        if nums1[i1 - 1] < nums2[i2 - 1]:
            return self.findKthNum(nums1[i1:], m - i1, nums2, n, k - i1)
        elif nums1[i1 - 1] > nums2[i2 - 1]:
            return self.findKthNum(nums1, m, nums2[i2:], n - i2, k - i2)
        else:
            return nums1[i1 - 1]
