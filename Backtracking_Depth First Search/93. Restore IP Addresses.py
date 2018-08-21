# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


# idea: backtracking and prune the wrong answer.
# A valid snippet is defined as:
# 1. s[i]
# 2. s[i:i+1]，s[i] !=0
# 3. s[i:i+2]，s[i] != 0，and s[i:i+2] <= 255
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        self.ans = []
        self.find_ip('', s, 4)
        return self.ans

    def find_ip(self, prev_ans, remain_s, remain_choice):
        if remain_choice == 0 and remain_s == '':
            self.ans.append(prev_ans[:-1])
            return
        if remain_choice == 0:
            return
        for i in range(1, 4):
            if len(remain_s) >= i:
                if self.is_valid(remain_s[:i]):
                    self.find_ip(prev_ans + remain_s[:i] + '.', remain_s[i:],
                                 remain_choice - 1)

    def is_valid(self, s):
        if len(s) == 1:
            return True
        if len(s) == 2 and s[0] != '0':
            return True
        if len(s) == 3 and s[0] != '0' and int(s) <= 255:
            return True
        return False
