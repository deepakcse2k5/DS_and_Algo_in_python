from __future__ import print_function
from collections import deque

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left,self.right, self.next = None, None, None
        
    def print_tree(self):
        print("Traversal using 'next' pointer:",end='')
        current = self
        while current:
            print(str(current.val)+ " ", end=" ")
            current = current.next
            
def connect_all_siblings(root):
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    currNode, prevNode = None,None
    while queue:
        currNode = queue.popleft()
        if prevNode:
            prevNode.next = currNode
        prevNode = currNode
        
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)
            
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()

        