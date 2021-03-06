# Rearrange a LinkedList

# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that
# the nodes from the second half of the LinkedList are inserted alternately to the nodes
# from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# , method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
# Time complexity - O(N) and space complexity - O(1)


from __future__ import print_function

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        
    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value)+ " ",end ='')
            temp = temp.next
        print()
        
def reorder(head):
    if head is None and head.next is  None:
        return None
    slow , fast = head , head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    head_second_half = reverse(slow)
    
    head_first_half = head
    
    while head_first_half is not None and head_second_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp
        
        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp
        
    if head_first_half is not None:
        head_first_half.next= None      
        
def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    reorder(head)
    head.print_list()
    
    
    
main()
    
    
