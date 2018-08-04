# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums = set(nums)
        longestConsec = 0
        for num in setNums.copy():
            if num not in setNums:
                continue
            leftConsec, tmpLeft = 0, num - 1
            while tmpLeft in setNums:
                setNums.remove(tmpLeft)
                tmpLeft -= 1
                leftConsec += 1
            rightConsec, tmpRight = 0, num + 1
            while tmpRight in setNums:
                setNums.remove(tmpRight)
                tmpRight += 1
                rightConsec += 1
            if leftConsec + rightConsec + 1 > longestConsec:
                longestConsec = leftConsec + rightConsec + 1
            setNums.remove(num)
        return longestConsec


# Another Version:
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
