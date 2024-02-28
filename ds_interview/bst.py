class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val) -> None:
        self.root = TreeNode(val)

    def insert(self, node, val):
        if node is not None:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    self.insert(node.left,val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    self.insert(node.right, val)
        else:
            self.root = TreeNode(val)
        return
        