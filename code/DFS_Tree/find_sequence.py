class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    # TODO: Write your code here
    if not root:
        return len(sequence)==0
    return find_path_recursive(root, sequence, 0)


def find_path_recursive(currNode, sequence, sequenceIndex):
    if currNode is None:
        return False

    seqLen = len(sequence)

    if sequenceIndex>=seqLen or currNode.val != sequence[sequenceIndex]:
        return False

    if currNode.left is None and currNode.right is None and sequenceIndex==seqLen -1:
        return True

    return find_path_recursive(currNode.left, sequence, sequenceIndex+1) or find_path_recursive(currNode.right, sequence, sequenceIndex+1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()


# Time complexity - O(N) and space complexity - O(N) because we traverse all the nodes in worst case scenario
