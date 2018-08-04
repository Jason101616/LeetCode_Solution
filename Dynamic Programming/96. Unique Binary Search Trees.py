# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

'''
idea: We can know that by zero we can have 1 bst of null
by 1 we have 1 bst of 1
and n = 2, answer is 2
Now idea is simple for rest numbers. for n=3 make 1 as root node so there will be 0 nodes in left subtree and 2 nodes in right subtree. we know the solution for 2 nodes that they can be used to make 2 bsts.
Now making 2 as the root node , there will be 1 in left subtree and 1 node in right subtree. 1 node results in 1 way for making a BST.
Now making 3 as root node. There will be 2 nodes in left subtree and 0 nodes in right subtree. We know 2 will give 2 BST and zero will give 1 BST.
Totalling the result of all the 3 nodes as root will give 5. Same process can be applied for more numbers.
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = [1 for _ in range(n + 1)]
        for numNode in range(1, n + 1):
            cur = 0
            for i in range(numNode):
                numLeftNode = res[i]
                numRightNode = res[numNode - 1 - i]
                cur += numLeftNode * numRightNode
            res[numNode] = cur
        return res[-1]
