# idea: 首先选出k值为0且身高最低的人，记为hi, ki，将其加入结果集。
# 然后更新队列，若队列中人员的身高≤hi，则令其k值 - 1（需要记录原始的k值）。
# 循环直到队列为空。
# time complexity: O(n * n * log(n))
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people.sort(key=lambda x: (x[1], x[0]))
        for i in range(len(people)):
            people[i].append(people[i][1])
        ans = []
        while people:
            ans.append(people[0][:2])
            cur_height = people[0][0]
            del people[0]
            for i in range(len(people)):
                if people[i][0] <= cur_height:
                    people[i][2] -= 1
            people.sort(key=lambda x: (x[2], x[0]))
        return ans
