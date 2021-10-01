class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_recursive(root, S, [])


def count_paths_recursive(currNode, S, currPath):
    if currNode is None:
        return 0
    # add the current node to the path
    currPath.append(currNode.val)

    pathCount, pathSum = 0, 0
    # find the sums of all sub-paths in the current path list
    for i in range(len(currPath) - 1, -1, -1):
        pathSum += currPath[i]
        # if the sum of any sub-path is equal to 'S' we increment our path count.
        if pathCount == S:
            pathCount += 1
        # traverse left subtree
    pathCount += count_paths_recursive(currNode.left, S, currPath)
    # traverse right subtree
    pathCount += count_paths_recursive(currNode.right, S, currPath)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    del currPath[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
