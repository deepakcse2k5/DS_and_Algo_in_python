# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

# Time complextity O(N) and O(1)

class Node:
    def __init__(self,value) :
        self.value = value
        self.next = None
        
# Brute Force approach
def find_middle_of_linked_list1(head):
    count =0
    while head is not None:
        head = head.next
        count = count+1    
    if (count%2)==0:
        return count//2 + 1
    else:
        return count//2 +1
    
# slow and fast pointer approach
def find_middle_of_linked_list(head):
    slow, fast = head , head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow



def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("Middle of the linked list",find_middle_of_linked_list(head).value)
    
    print("Middle of the linked list",find_middle_of_linked_list1(head))
    
    head.next.next.next.next.next = Node(6)
    
    print("Middle of the linked list",find_middle_of_linked_list(head).value)
    
    print("Middle of the linked list",find_middle_of_linked_list1(head))
    
main()