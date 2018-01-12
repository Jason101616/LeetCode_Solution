# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

class Str_compare(str):
    def __lt__(self, other):
        return self + other > other + self
    
class Solution:
    # @param {integer[]} nums
    # @return {string}
    
    def largestNumber(self, nums):
        nums = ''.join(sorted(map(str, nums), key=Str_compare))
        return '0' if nums[0] == '0' else nums