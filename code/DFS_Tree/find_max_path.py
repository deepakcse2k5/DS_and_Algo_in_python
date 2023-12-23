# Given a binary tree, find the root-to-leaf path with the maximum sum.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_max_path(root):

    sum = root.val

    find_max_path_recursive(root, sum, [] )
    return sum


def find_max_path_recursive(currNode,curr_sum, currPath):
    max_sum = curr_sum
    # edge case
    if currNode is None:
        return None

    # max_sum = curr_sum + currNode.val
    currPath.append(currNode.val)

    if  currNode.left is None and currNode.right is None:
        curr_sum = sum(currPath)
        if curr_sum > max_sum:
            max_sum = curr_sum

        # allPath.append(list(currPath))
    else:
        find_max_path_recursive(currNode.left, curr_sum+currNode.val, currPath)

        find_max_path_recursive(currNode.right, curr_sum+currNode.val, currPath)

    del currPath[-1]



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths with sum " + str(sum) + ": " + str(find_max_path(root)))


main()


