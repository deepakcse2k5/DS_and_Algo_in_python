# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case:
        if subRoot is None:
            return True

        if root is None:
            return False

        def areSimilar(root1, root2):
            # Base case
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False

            # check if data of both roots are same and data of left and right subtree should be also same
            return (root1.val == root2.val and areSimilar(root1.left, root2.left) and areSimilar(root1.right,
                                                                                                 root2.right))

        # check tree with root as current None
        if (areSimilar(root, subRoot)):
            return True
        # if root of the trees doesn't match , check with left and right subtree
        return areSimilar(root.left, subRoot) or areSimilar(root.right, subRoot)
