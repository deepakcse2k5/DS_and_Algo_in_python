class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def helper(x,y):
    if (x is None and y is None):
        return True
    elif ( x is None or y is None):
        return False
    return x.val==y.val and helper(x.left,y.right) and helper(x.right,y.left)
def is_mirror(root):
    if root is None:
        return True
    return helper(root.left, root.right)



