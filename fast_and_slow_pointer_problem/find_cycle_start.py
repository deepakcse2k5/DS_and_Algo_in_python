# Find the start of Linked list cycle
# Time complexity- O(N) and Space complexity - O(1)
from __future__ import print_function

class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None
        
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value,end='')
            temp = temp.next
        print()
        
def find_cycle_length(head):
    slow , fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow==fast:
            return calculate_cycle_length(slow)
    return 0
    
def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length +=1
        if current==slow:
            break
    return cycle_length

def find_cycle_start(head):
    k = find_cycle_length(head)
    p1 , p2 = head , head
    while k>0:
        p2 = p2.next
        k-=1
    while (p1!=p2):
        p1 = p1.next
        p2 = p2.next
    return p1

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    
    
main()