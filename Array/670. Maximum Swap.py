# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]

# idea:
# 我们希望置换后的数字最大，那么肯定最好高位上的小数字和低位上的大数字进行置换，比如题目汇总的例子1。
# 而如果高位上的都是大数字，像例子2那样，很有可能就不需要置换。所以我们需要找到每个数字右边的最大数字(包括其自身)，
# 这样我们再从高位向低位遍历，如果某一位上的数字小于其右边的最大数字，说明需要调换，由于最大数字可能不止出现一次，
# 我们希望能跟较低位的数字置换，这样置换后的数字最大，所以我们就从低位向高位遍历来找那个最大的数字，找到后进行调换即可。
# 比如对于1993这个数：

# 1 9 9 3

# 9 9 9 3  (back数组)

# 9 9 1 3

# 我们建立好back数组后，从头遍历原数字，发现1比9小，于是从末尾往前找9，找到后一置换，就得到了9913。
# time: O(n)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        res = copy.deepcopy(num_list)
        # update num_list
        # recursive equation is: num_list[i] = max(num_list[i], num_list[i + 1])
        for i in range(len(num_list) - 2, -1, -1):
            num_list[i] = max(num_list[i], num_list[i + 1])
        # traverse from the left to right, find the index of the first number less than num_list
        for i in range(len(num_list)):
            if res[i] == num_list[i]:
                continue
            # find this number
            for j in range(len(num_list) - 1, i, -1):
                if res[j] == num_list[i]:
                    res[j], res[i] = res[i], res[j]
                    return int(''.join(res))
        return int(''.join(res))

# written by me:
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        larger_than = [0 for _ in range(len(num))]
        larger_than[-1] = num[-1]
        for i in range(len(num) - 2, -1, -1):
            larger_than[i] = max(larger_than[i + 1], num[i])
        for i in range(len(num)):
            if num[i] < larger_than[i]:
                left = i
                for j in range(len(num) - 1, i, -1):
                    if num[j] == larger_than[i]:
                        right = j
                        break
                num[left], num[right] = num[right], num[left]
                break
        return int(''.join(num))