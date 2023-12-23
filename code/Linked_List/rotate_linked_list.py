from __future__ import print_function

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val,end=' ')
            temp = temp.next


def rotate_linked_list(head, k):
    if k<1 and head is None:
        return head

    curr , prev = head , None
    i =0
    first_node_of_prev_part = head
    while curr is not None and i<k:
        prev = curr
        curr = curr.next
        i+=1
    first_node_of_rotate_list = curr
    while curr is not None:
        last_node_of_rotate_list = curr
        curr = curr.next

    last_node_of_rotate_list.next = first_node_of_prev_part
    prev.next = None
    return first_node_of_rotate_list


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Node of original linked list :",end='')
    head.print_list()
    result = rotate_linked_list(head,3)
    print("Node of rotated linked list :",end ='')
    result.print_list()


main()
