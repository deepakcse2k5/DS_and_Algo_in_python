from collections import deque


class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left , self.right = None, None
        
def find_largest_value(root):
    result = deque()
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    
    while queue:
        levelSize = len(queue)
        maxVal = 0.0
        for _ in range(levelSize):
            currentNode = queue.popleft()
            maxVal = max(maxVal,currentNode.val)
            
            if currentNode.left:
                queue.append(currentNode.left)
                
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(maxVal)
        
    return result
    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Largest values  are: " + str(find_largest_value(root)))


main()