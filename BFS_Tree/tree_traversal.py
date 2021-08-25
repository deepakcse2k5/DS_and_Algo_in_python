from collections import deque


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    
def traverse(root):
    result =[]
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
                
        result.append(currentLevel)
            
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(7)
    print("Level order traversal:"+str(traverse(root)))
    
    
main()
        
    
    
    
# Time complexity
# The time complexity of the above algorithm is O(N), 
# where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.


# Space complexity
# The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
# We will also need O(N) space for the queue. 
# Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
# therefore we will need
# O(N) space to store them in the queue.