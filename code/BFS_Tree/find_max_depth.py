from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_max_depth(root):
  # TODO: Write your code here
    result = deque()
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    maxTreeDepth =0
    while queue:
        maxTreeDepth +=1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            
            # if not currentNode.left and not currentNode.right :
            #     return minTreeDepth
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
                
    return maxTreeDepth


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Max Depth: " + str(find_max_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Max Depth: " + str(find_max_depth(root)))


main()