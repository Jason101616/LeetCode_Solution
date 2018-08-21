# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

# brute force. maximum number of attempts is 4 * 4 * 4 * 4
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = {int(time[0]), int(time[1]), int(time[3]), int(time[4])}
        if len(nums) == 1:
            return time
        nums = list(nums)
        self.res = ""
        self.maxDiff = float('inf')
        self.dfs(nums, [], 60 * int(time[0: 2]) + int(time[3: 5]), 0)
        return self.res

    def dfs(self, nums, curRes, target, idx):
        if len(curRes) == 4:
            tmpRes = 60 * (10 * curRes[0] + curRes[1]) + 10 * curRes[2] + curRes[3]
            tmpDiff = tmpRes - target if tmpRes > target else 1440 + tmpRes - target
            if tmpDiff < self.maxDiff:
                self.maxDiff = tmpDiff
                self.res = str(curRes[0]) + str(curRes[1]) + ':' + str(curRes[2]) + str(curRes[3])
        else:
            for num in nums:
                if idx == 0 and num > 2:
                    continue
                if idx == 1 and 10 * curRes[0] + num > 23:
                    continue
                if idx == 2 and num > 5:
                    continue
                if idx == 3 and 10 * curRes[2] + num > 59:
                    continue
                self.dfs(nums, curRes + [num], target, idx + 1)

