from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Solution 1: level-order traversal
# if meet a None node. The same level node in the right of it must all be None node
# the next level must all be None Node
def check_complete_bt(root):
    queue = deque()
    queue.append(root)
    while queue:
        is_last_level = False
        cur_len = len(queue)
        for i in range(cur_len):
            cur_node = queue.popleft()
            if not cur_node:
                is_last_level = True
            else:
                if is_last_level:
                    return False
                else:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
        if is_last_level:
            for i in range(len(queue)):
                if queue.popleft() != None:
                    return False
    return True


if __name__ == '__main__':
    node0 = TreeNode()
    node1 = TreeNode()
    node2 = TreeNode()
    node0.right = node2
    ans = check_complete_bt(node0)
    print(ans)
    node0.left = node1
    ans = check_complete_bt(node0)
    print(ans)
    node0.right = None
    ans = check_complete_bt(node0)
    print(ans)


# Solution 2: recursive solution
# http://www.geeksforgeeks.org/check-whether-binary-tree-complete-not-set-2-recursive-solution/
# the main idea is calculate the number of nodes of the current tree, and assign each node an index.
# If this tree is a valid complete tree, the index must meet some requirements.
# This function counts the number of nodes in a binary tree
def countNodes(root):
    if root is None:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))


# This function checks if binary tree is complete or not
def isComplete(root, index, number_nodes):
    # An empty is complete
    if root is None:
        return True

    # If index assigned to current nodes is more than
    # number of nodes in tree, then tree is not complete
    if index >= number_nodes:
        return False

    # Recur for left and right subtress
    return (isComplete(root.left, 2 * index + 1, number_nodes)
            and isComplete(root.right, 2 * index + 2, number_nodes))


# Driver Program

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

node_count = countNodes(root)
index = 0

if isComplete(root, index, node_count):
    print("The Binary Tree is complete")
else:
    print("The Binary Tree is not complete")
