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


def reverse_sub_list(head, p, q):
    prev = None
    curr = head
    count = 0
    while curr is not None and count < p-1:
        prev = curr
        curr = curr.next
        count += 1
    last_node_of_first_part = prev
    last_node_of_sub_list = curr
    count = 0
    next = None
    while curr is not None and count < q-p+1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    if last_node_of_first_part is not None:
        last_node_of_first_part.next= prev
    else:
        head = prev
    last_node_of_sub_list.next = curr
    return  head



def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
