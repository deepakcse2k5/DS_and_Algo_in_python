class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

def inorder(node):
    if node is None:
        return []
    else:
        return inorder(node.left) + [node.val]+ inorder(node.right)
    
def preorder(node):
    if node is None:
        return []
    else:
        return [node.val] + preorder(node.left) + preorder(node.right)
    
def postorder(node):
    if node is None:
        return []
    else:
        return postorder(node.left) + postorder(node.right) + [node.val]
