class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path(root, sum):
    if root is None:
        return False
    if root.val == sum and root.left is None and root.right is None:
        return True
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()


# Time complexity#

# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space complexity#

# The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
