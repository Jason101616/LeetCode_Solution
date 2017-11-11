# Solution 1: DFS. Child knows its height
def find_height(root):
    height = find_height_dfs(root, 0)
    return height


def find_height_dfs(node, height):
    if not node:
        return height
    left = find_height_dfs(node.left, height + 1)
    right = find_height_dfs(node.right, height + 1)
    return max(left, right)


# Solution 2: recursion. Root knows its height
def find_height(root):
    if not root:
        return 0
    left = find_height(root.left) + 1
    right = find_height(root.right) + 1
    return max(left, right)