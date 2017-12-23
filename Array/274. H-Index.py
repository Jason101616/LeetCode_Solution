# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

# Note: If there are several possible values for h, the maximum one is taken as the h-index.

# Solution 1: sort
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse=True)
        i = 0
        find_ans = False
        for i in range(len(citations)):
            if citations[i] < i + 1:
                find_ans = True
                break
        return i if find_ans else i + 1

# Solution 2: counting sort 
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        cnt_list = [0 for _ in range(len(citations) + 1)]
        # citation > len(citations) can be cut off to len(citations), this will not affect the final result
        for citation in citations:
            cnt_list[min(citation, len(citations))] += 1
        cnt_sum = 0
        i = 0
        for i in range(len(cnt_list) - 1, -1, -1):
            cnt_sum += cnt_list[i]
            if cnt_sum >= i:
                break
        return i
            