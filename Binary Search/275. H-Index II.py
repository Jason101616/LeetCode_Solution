# Follow up for 274.H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
# binary search
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        l, r = 0, len(citations)
        while l < r:
            m = l + (r - l) // 2
            if len(citations) - m <= citations[m]:
                r = m
            else:
                l = m + 1
        return len(citations) - l