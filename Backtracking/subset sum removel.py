# Akuna capital OA
# idea: use backtracking
class Solution(object):
    def find_the_ans(self, my_list):
        self.my_ans = len(my_list)
        self.subset_removal(my_list)
        return self.my_ans

    def subset_removal(self, my_list):
        if len(my_list) < self.my_ans:
            self.my_ans = len(my_list)
        remove_list = self.combinationSum(my_list)
        if not remove_list:
            return
        for i in remove_list:
            cur_sum = sum(i)
            cur_remove = []
            for j in i:
                my_list.remove(j)
                cur_remove.append(j)
            my_list.remove(cur_sum)
            cur_remove.append(cur_sum)
            self.subset_removal(my_list)
            for j in cur_remove:
                my_list.append(j)

    def combinationSum(self, candidates):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        self.candidates = sorted(candidates)
        self.candidates_len = len(candidates)
        self.ans = []
        for i, target in enumerate(self.candidates):
            self.find_ans([], 0, 0, target, i)
        return self.ans

    def find_ans(self, cur_list, cur_sum, index, target, t_index):
        if cur_sum == target:
            self.ans.append(cur_list)
            return
        if cur_sum > target:
            return
        for i in range(index, self.candidates_len):
            if i != t_index:
                self.find_ans(cur_list + [self.candidates[i]],
                              cur_sum + self.candidates[i], i + 1, target,
                              t_index)


if __name__ == "__main__":
    test = Solution()
    my_list = [48, 20, 1, 3, 4, 6, 9, 24]
    ans = test.find_the_ans(my_list)
    print(ans)
