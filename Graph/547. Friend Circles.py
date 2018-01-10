# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

# Example 1:
# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

# idea: build the graph and find connected component
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # build the graph from M
        graph = collections.defaultdict(lambda: set())
        for r_i, row in enumerate(M):
            for c_i in range(r_i + 1, len(M[r_i])):
                if M[r_i][c_i] == 1:
                    graph[r_i].add(c_i)
                    graph[c_i].add(r_i)
        # find connected part from the graph by BFS, DFS, union find
        visited = set()
        circle = 0
        for i in range(len(M)):
            if i not in visited:
                circle += 1
                q = collections.deque()
                q.append(i)
                visited.add(i)
                while q:
                    cur_person = q.popleft()
                    for j in graph[cur_person]:
                        if j not in visited:
                            q.append(j)
                            visited.add(j)
        return circle