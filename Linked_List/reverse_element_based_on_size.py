from __future__ import print_function


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end="")
            temp = temp.next
        print()


def get_length(head):
    count = 0
    curr = head
    while curr is not None:
        curr = curr.next
        count += 1
    return count


def reverse(head, p, q):
    curr = head
    prev, next = None, None
    i = 0
    while curr is not None and i<p-1:
        prev = curr
        curr = curr.next
        i+=1
    last_node_of_first_part = prev
    last_node_of_sub_list = curr
    i = 0
    while curr is not None and i<q-p+1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = prev
    else:
        head = prev
    # if last_node_of_sub_list is not None:
    last_node_of_sub_list.next = curr
    return head


def reverse_element_based_on_size(head):
    n = get_length(head)
    print("length of linked list",n)
    if n % 2 == 0:
        head = reverse(head, 1, n / 2)
        head = reverse(head, n / 2 + 1, n)
    else:
        head = reverse(head, 1, n//2)
        # print("*****")
        # head.print_list()
        head = reverse(head, n // 2 + 2, n)
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Node of original linked list", end='')
    head.print_list()
    print(get_length(head))
    # result = reverse(head,1,2)
    print("Node of reverse linked list :", end='')
    # result.print_list()
    result1 = reverse_element_based_on_size(head)
    print("Node of reverse linked list based on size:", end='')
    result1.print_list()


main()
