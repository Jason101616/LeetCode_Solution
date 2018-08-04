# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# For example, you may serialize the following tree

#     1
#    / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: preorder traversal and then preversal recovery.
# careful the trick of trace the change of index
class Codec:
    def __preorder_serial(self, root, serial_list):
        if root:
            serial_list.append(str(root.val))
            self.__preorder_serial(root.left, serial_list)
            self.__preorder_serial(root.right, serial_list)
        else:
            serial_list.append('None')

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial_list = []
        self.__preorder_serial(root, serial_list)
        return ' '.join(serial_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        deserial_list = data.split(' ')
        for i in range(len(deserial_list)):
            if deserial_list[i] == 'None':
                deserial_list[i] = None
            else:
                deserial_list[i] = int(deserial_list[i])
        index = -1
        return self.__preorder_deserial(deserial_list, index)[0]

    def __preorder_deserial(self, tree_list, index):
        index += 1
        if index >= len(tree_list) or tree_list[index] == None:
            return None, index
        new_node = TreeNode(tree_list[index])
        new_node.left, index = self.__preorder_deserial(tree_list, index)
        new_node.right, index = self.__preorder_deserial(tree_list, index)
        return new_node, index

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
