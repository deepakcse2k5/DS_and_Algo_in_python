from __future__ import print_function

from collections import deque

class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left , self.right,self.next = None, None, None
    
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()
      
def connect_level_order_sibling(root):
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    
    while queue:
        levelSize = len(queue)
        prevNode = None
        for _ in range(levelSize):
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
    connect_level_order_sibling(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
                
        