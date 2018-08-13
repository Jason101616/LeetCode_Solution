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
# time: O(n^2*logk)
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


# Approach 2: Binary search(Java)
# time: O(nlgn*lgX), X is the gap between biggest value and smallest value
# public class Solution {
#     public int kthSmallest(int[][] matrix, int k) {
#         int lo = matrix[0][0], hi = matrix[matrix.length - 1][matrix[0].length - 1] + 1;//[lo, hi)
#         while(lo < hi) {
#             int mid = lo + (hi - lo) / 2;
#             int count = 0;
#             for(int i = 0; i < matrix.length; i++) {
#                 int l = 0, r = matrix[i].length;
#                 while (l < r) {
#                     int m = l + (r - l) / 2;
#                     if(matrix[i][m] > mid) r = m;
#                     else l = m + 1;
#                 }
#                 count += l;
#             }
#             if(count < k) lo = mid + 1;
#             else hi = mid;
#         }
#         return lo;
#     }
# }

# public class Solution {
#     public int kthSmallest(int[][] matrix, int k) {
#         int lo = matrix[0][0], hi = matrix[matrix.length - 1][matrix[0].length - 1] + 1;//[lo, hi)
#         while(lo < hi) {
#             int mid = lo + (hi - lo) / 2;
#             int count = 0,  j = matrix[0].length - 1;
#             for(int i = 0; i < matrix.length; i++) {
#                 while(j >= 0 && matrix[i][j] > mid) j--;
#                 count += (j + 1);
#             }
#             if(count < k) lo = mid + 1;
#             else hi = mid;
#         }
#         return lo;
#     }
# }