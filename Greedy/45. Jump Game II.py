# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
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
        if len(nums) == 1:
            return 0
        step, max_pos, next_max_pos = 1, nums[0], nums[0]
        for i in range(1, len(nums)):
            if max_pos >= len(nums) - 1:
                return step
            if i > max_pos:
                max_pos = next_max_pos
                step += 1
            next_max_pos = max(next_max_pos, i + nums[i])
        return step
