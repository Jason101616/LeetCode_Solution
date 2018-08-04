# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.

# Approach 1: Priority Queue(heap)
import Queue


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pq = Queue.PriorityQueue()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                pq.put(-matrix[i][j])
                if pq.qsize() > k:
                    pq.get()
        return -pq.get()


# Approach 2: Binary search(C++)
# time: O(nlgn*lgX), X is the gap between biggest value and smallest value
class Solution {
public:
    int


kthSmallest(vector < vector < int >> & matrix, int
k) {
    int
left = matrix[0][0], right = matrix.back().back();
while (left < right) {
int mid = left + (right - left) / 2, cnt = 0;
for (int i = 0; i < matrix.size(); ++i) {
cnt += upper_bound(matrix[i].begin(), matrix[i].end(), mid) - matrix[i].begin();
# Returns an iterator pointing to the first element in the range [first,last) which compares greater than val.
# Python中对应的函数是bisect_right
}
if (cnt < k) left = mid + 1;
else right = mid;
}
return left;
}
};
