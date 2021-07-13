# Palindrome LinkedList

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false
# Time complexity - O(N) and space complexity - O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

def is_palindromic_linked_list(head):
    slow , fast = head , head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    head_second_half = reverse(slow)
    
    copy_head_second_half = head_second_half
    
    while head is not None and head_second_half is not None:
        if head.value!= head_second_half.value:
            break
        head = head.next
        head_second_half = head_second_half.next
        
    reverse(copy_head_second_half)
    
    if head is None or head_second_half is None:
        return True
    
    return False


def reverse(head):
    prev = None
    
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    
    print(is_palindromic_linked_list(head))
    head.next.next.next.next.next = Node(1)
    print(is_palindromic_linked_list(head))
    
main()
