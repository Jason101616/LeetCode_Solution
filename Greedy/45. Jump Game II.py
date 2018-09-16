# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:
#
# You can assume that you can always reach the last index.

# Approach 1: BFS, TLE
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [False for _ in range(len(nums))]
        q = collections.deque()
        q.append(0)
        visited[0] = True
        step = 0
        while q:
            cur_level = len(q)
            find_ans = False
            for i in range(cur_level):
                cur_point = q.popleft()
                if cur_point == len(nums) - 1:
                    find_ans = True
                    break
                if cur_point + nums[cur_point] >= len(nums) - 1:
                    step += 1
                    find_ans = True
                    break
                for j in range(cur_point + 1, cur_point + 1 + nums[cur_point]):
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
            if find_ans:
                break
            step += 1
        return step


# Approach 2: Greedy
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        canReachMaxIdx = nums[0]
        if canReachMaxIdx >= len(nums) - 1:
            return 1

        nextReachMax, curJump = 0, 1
        for i, length in enumerate(nums):
            if i > canReachMaxIdx:
                canReachMaxIdx = nextReachMax
                curJump += 1

            nextReachMax = max(nextReachMax, i + length)
            if nextReachMax >= len(nums) - 1:
                return curJump + 1
