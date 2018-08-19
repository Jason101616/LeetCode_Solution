# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# Example 1:
#
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# Example 2:
#
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false

# version 1: add O(1), find O(n)

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = dict()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.nums:
            self.nums[number] = 0
        self.nums[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.nums:
            if value - num in self.nums:
                if value - num != num and self.nums[value - num] >= 1:
                    return True
                if value - num == num and self.nums[num] >= 2:
                    return True
        return False

# version 2: add O(n) find O(1). TLE in OJ.
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()
        self.sums = set()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.nums:
            self.sums.add(number * 2)
        else:
            for num in self.nums:
                self.sums.add(num + number)
            self.nums.add(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        return value in self.sums
