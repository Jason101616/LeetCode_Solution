# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


# Solution 1: DFS
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        cur_remain_num = []
        self.target = n
        for i in range(10):
            cur_remain_num.append(i)
        self.cnt = 0
        self.cnt_unique_num([], 1, cur_remain_num)
        return self.cnt

    def cnt_unique_num(self, cur_num, cur_level, cur_remain_num):
        if cur_level == self.target or not cur_remain_num:
            self.cnt += len(cur_remain_num)
            return
        for num in cur_remain_num:
            self.cnt += 1
            if cur_level == 1 and num == 0:
                continue
            cur_remain_num.remove(num)
            self.cnt_unique_num(cur_num + [num], cur_level + 1, cur_remain_num)
            cur_remain_num.append(num)
            cur_remain_num.sort()

# Solution 2: count the number directly
# Let f(n) = count of number with unique digits of length n.

# f(1) = 10. (0, 1, 2, 3, ...., 9)

# f(2) = 9 * 9. Because for each number i from 1, ..., 9, we can pick j to form a 2-digit number ij and there are 9 numbers that are different from i for j to choose from.

# f(3) = f(2) * 8 = 9 * 9 * 8. Because for each number with unique digits of length 2, say ij, we can pick k to form a 3 digit number ijk and there are 8 numbers that are different from i and j for k to choose from.

# Similarly f(4) = f(3) * 7 = 9 * 9 * 8 * 7....

# ...

# f(10) = 9 * 9 * 8 * 7 * 6 * ... * 1

# f(11) = 0 = f(12) = f(13)....

# any number with length > 10 couldn't be unique digits number.

# The problem is asking for numbers from 0 to 10^n. Hence return f(1) + f(2) + .. + f(n)
