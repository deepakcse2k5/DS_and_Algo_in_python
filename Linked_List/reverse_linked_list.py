from __future__ import print_function
class Node:
    def __init__(self,value) :
        self.value = value
        self.next = None
        
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value,end =" ")
            temp = temp.next
            
def reverse(head):
    pass


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next = Node(8)
    head.next.next = Node(10)
    
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
        
        
main()
