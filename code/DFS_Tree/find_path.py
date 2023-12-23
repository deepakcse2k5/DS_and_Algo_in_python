class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    find_path_recursive(root, sum, [], allPaths)
    return allPaths


def find_path_recursive(currNode, required_sum, currPath, allPaths):
    if currNode is None:
        return
    # add current node to the path
    currPath.append(currNode.val)

    # if current node is leaf and equal to required sum then save the current path
    if currNode.val == required_sum and currNode.left is None and currNode.right is None:
        allPaths.append(list(currPath))
    else:
        # traverse left subtree
        find_path_recursive(currNode.left, required_sum - currNode.val, currPath, allPaths)

        # traverse right subtree
        find_path_recursive(currNode.right, required_sum - currNode.val, currPath, allPaths)
    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del currPath[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


main()

# Time complexity#

# The time complexity of the above algorithm is O(N^2), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once (which will take O(N)),
# and for every leaf node, we might have to store its path (by making a copy of the current path) which will take O(N).

# We can calculate a tighter time complexity of O(NlogN) from the space complexity discussion below.
# Space complexity#

# If we ignore the space required for the allPaths list, the space complexity of the above algorithm will be O(N) in the worst case.
# This space will be used to store the recursion stack.
# The worst-case will happen when the given tree is a linked list (i.e., every node has only one child).
