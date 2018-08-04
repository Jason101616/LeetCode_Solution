def findKthSmallest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while True:
        pos = partition(nums, left, right)
        if pos == k - 1:
            return nums[pos]
        if pos > k - 1:
            right = pos - 1
        else:
            left = pos + 1


def partition(nums, left, right):
    pivot_pos, pivot_val = left, nums[left]
    for i in range(left + 1, right + 1):
        if nums[i] < pivot_val:
            pivot_pos += 1
            if pivot_pos != i:
                nums[pivot_pos], nums[i] = nums[i], nums[pivot_pos]
    nums[left] = nums[pivot_pos]
    nums[pivot_pos] = pivot_val
    return pivot_pos


# idea: Manhattan Distance can be computed by x axis and y axis respectively. Then the problem goes down to 1 dimension.
# In 1-d, just pick the middle number as the meeting point
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # extract the x and y coordinate of each 1 node
        x_coor, y_coor = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    x_coor.append(i)
                    y_coor.append(j)
        # calculate the distance in 1-d array
        # calculate the middle point of the 1-d array as the meeting point in that dimension
        res = 0
        mid_index_x = len(x_coor) // 2
        for x in x_coor:
            res += abs(x - x_coor[mid_index_x])

        # y_coor.sort()
        # mid_index_y = len(y_coor) // 2
        # for y in y_coor:
        #     res += abs(y - y_coor[mid_index_y])
        mid_index_y = len(y_coor) // 2 + 1
        mid_y = findKthSmallest(y_coor, mid_index_y)  # avoid sort in the place, use divide and conquer
        for y in y_coor:
            res += abs(y - mid_y)
        return res
