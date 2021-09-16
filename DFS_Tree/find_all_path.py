# Given a binary tree, return all root-to-leaf paths.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_all_path(root):
    all_paths = []
    find_all_path_recursive(root, [], all_paths)
    return all_paths


def find_all_path_recursive(currNode, currPath, allPaths):
    if currNode is None:
        return

    currPath.append(currNode.val)

    if currNode.left is  None and currNode.right is  None:
        allPaths.append(list(currPath))

    else:
        find_all_path_recursive(currNode.left, currPath, allPaths)

        find_all_path_recursive(currNode.right, currPath, allPaths)

    del currPath[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths with sum " + str(sum) + ": " + str(find_all_path(root)))


main()
