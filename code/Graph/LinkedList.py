from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    # insert value at the start of the linked list
    def insert_at_head(self,new_node):
        temp = Node(new_node)
        if self.head is None:
            self.head = temp
            return self.head
        else:
            temp.next = self.head
            self.head = temp
            return self.head

    # insert value at the end of linked list
    def insert_at_end(self, value):
        # create new node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            temp = self.get_head()
            while temp.next is not None:
                

