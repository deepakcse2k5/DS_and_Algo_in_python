class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root):
    return find_sum_recursive(root, 0)


def find_sum_recursive(currNode, pathSum):
    if currNode is None:
        return 0

    pathSum = 10 * pathSum + currNode.val

    if currNode.left is None and currNode.right is None:
        return pathSum

    return find_sum_recursive(currNode.left, pathSum) + find_sum_recursive(currNode.right, pathSum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print("Tree paths with sum " + str(sum) + ": " + str(path_sum(root)))


main()

# Time complexity - O(N) and Space complexity- O(N) because we traverse each node
