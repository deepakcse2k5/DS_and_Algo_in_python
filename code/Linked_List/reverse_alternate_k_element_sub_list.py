from __future__ import print_function

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val,end='->')
            temp = temp.next
        print()


def reverse_alternate_k_element_sub_list(head,k):
    if k<1 and head is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        last_node_of_prev_part = prev
        last_node_of_sublist = curr
        next = None
        i =0
        while curr is not None and i<k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i+=1
        if last_node_of_prev_part is not None:
            last_node_of_prev_part.next = prev
        else:
            head = prev
        last_node_of_sublist.next = curr
        # skip k nodes
        i = 0
        while curr is not None and i<k:
            prev = curr
            curr = curr.next
            i+=1
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    print("Node of original linked list :",end='')
    head.print_list()
    print("Node after alternating every k element of sublist :",end='')
    result = reverse_alternate_k_element_sub_list(head,3)
    result.print_list()


main()
