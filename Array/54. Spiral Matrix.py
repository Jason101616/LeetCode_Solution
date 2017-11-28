# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


# use a dictionary to record whether each cell has been visited
# first go right until out of bound or meet a cell has been visited
# then turn down and move until cannot move downward
# then turn left and move until cannot move leftward
# then turn up and move until cannot move upward
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        ans = []
        row, col = len(matrix), len(matrix[0])
        visited = set()
        start = [0, 0]
        while len(visited) != row * col:
            while start[1] < col and tuple(start) not in visited:
                ans.append(matrix[start[0]][start[1]])
                visited.add(tuple(start))
                start[1] += 1
            start[0] += 1
            start[1] -= 1
            while start[0] < row and tuple(start) not in visited:
                ans.append(matrix[start[0]][start[1]])
                visited.add(tuple(start))
                start[0] += 1
            start[0] -= 1
            start[1] -= 1
            while start[1] >= 0 and tuple(start) not in visited:
                ans.append(matrix[start[0]][start[1]])
                visited.add(tuple(start))
                start[1] -= 1
            start[0] -= 1
            start[1] += 1
            while start[0] >= 0 and tuple(start) not in visited:
                ans.append(matrix[start[0]][start[1]])
                visited.add(tuple(start))
                start[0] -= 1
            start[0] += 1
            start[1] += 1
        return ans