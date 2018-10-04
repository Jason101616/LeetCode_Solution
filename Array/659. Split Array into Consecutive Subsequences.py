# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.
#
# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False
# Note:
# The length of the input is in range of [1, 10000]

# 1. We iterate through the array once to get the frequency of all the elements in the array
# 2. We iterate through the array once more and for each element we either see if it can be appended to a previously
# constructed consecutive sequence or if it can be the start of a new consecutive sequence. If neither are true,
# then we return false.

from collections import Counter, defaultdict
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = Counter(nums)
        follow = defaultdict(lambda: 0)
        for num in nums:
            if cnt[num] == 0:
                continue
            if follow[num]: # should not change location with next elif
                follow[num] -= 1
                follow[num + 1] += 1
            elif cnt[num + 1] and cnt[num + 2]:
                cnt[num + 1] -= 1
                cnt[num + 2] -= 1
                follow[num + 3] += 1
            else:
                return False
            cnt[num] -= 1
        return True