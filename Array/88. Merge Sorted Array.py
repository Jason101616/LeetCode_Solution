# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

# naive solution:
# 思路：两个index，根据大小放到一个新的数组中。然后将没有用完的数组插到新的数组后面。最后进行一次赋值。
# 42 ms
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tmp = [None] * (m + n)
        index_num1 = 0
        index_num2 = 0
        cnt = 0
        while index_num1 != m and index_num2 != n:
            if nums1[index_num1] < nums2[index_num2]:
                tmp[cnt] = nums1[index_num1]
                index_num1 += 1
                cnt += 1
            else:
                tmp[cnt] = nums2[index_num2]
                index_num2 += 1
                cnt += 1
        
        if index_num1 == m:
            tmp[cnt:] = nums2[index_num2:]
        else:
            tmp[cnt:] = nums1[index_num1:]
            
        for i in range(m + n):
            nums1[i] = tmp[i]

# inplace solution:
# 思路：从大的数开始比较，先插入到nums1的后面。
def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]