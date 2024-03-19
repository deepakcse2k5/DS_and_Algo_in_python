from linked_list_node import LinkedListNode

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def create_linked_list(self, lst):
        for i in reversed(lst):
            new_node = LinkedListNode(i)
            self.insert_node_at_head(new_node)

    def get_length(self, head):
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def get_node(self, head, index):
        temp = head
        for i in range(index):
            temp = temp.next
        return temp

    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        return result + "None"

