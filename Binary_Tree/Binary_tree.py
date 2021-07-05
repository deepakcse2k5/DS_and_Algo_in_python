class Queue(object):
    def __init__(self) :
        self.items = []
        
    def enque(self,item):
        self.items.insert(0,item)
        
    def is_empty(self):
        return len(self.items)==0
    
        
    def deque(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()
class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
        
    def preorder_print(self,start,traversal):
        # root->left -> right
        if start:
            traversal += (str(start.value)+ "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self,start,traversal):
        # left ->root-> right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value)+"-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self,start,traversal):
        # left -> right->root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value)+"-")
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "pre_order":
            return self.preorder_print(tree.root,"")
        elif traversal_type == "in_order":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "post_order":
            return self.postorder_print(tree.root, "")
        elif traversal_type =="levelorder":
            return self.level_order_print(tree.root)
        
        else:
            print("traversal type" +(str.traversal_type)+"is not supported")
            return False
        
    def level_order_print(self,start):
        if start is None:
            return
        queue = Queue()
        queue.enque(start)
        
        traversal = ""
        while len(queue)>0:
            traversal += str(queue.peek()) + "-"
            node = queue.deque()
            
            if node.left:
                queue.enque(node.left)
            if node.right:
                queue.enque(node.right)
        return traversal
    
    
    
    
# setup Binary Tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


# print(tree.print_tree("pre_order"))
# print(tree.print_tree("in_order"))
print(tree.print_tree("levelorder"))


    
