from __future__ import print_function


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()


def reverse_first_k_element(head, k):
    curr = head
    prev = None
    next = None
    i =0
    last_node_of_sub_list = curr
    while curr is not None and i<k-1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i+=1
    # head.print_list()
    last_node_of_sub_list.next = curr
    return prev


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Node of original linked list :", end=" ")
    head.print_list()
    result = reverse_first_k_element(head, 3)
    print("Node of reverse first k linked list :", end=" ")
    result.print_list()

main()
