from __future__ import print_function
from linked_list import LinkedList
from swap_two_nodes import swap
from print_list import print_list_with_forward_arrow


def swap_nodes(head, k):
    count = 0
    front, end = None, None
    curr = head
    while curr:
        count += 1
        if end is not None:
            end = end.next
        if count == k:
            front = curr
            end = head
        curr = curr.next
    swap(front, end)
    return head


def main():
    input_list = [
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]
    k = [2, 3, 2, 3, 1]
    for i in range(len(input_list)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])
        print(i + 1, ".\tOriginal linked list is: ", end="", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tk:", k[i])
        if k[i] <= 0:
            print("\tThe expected 'k' to have value from 1 \
                to length of the linked list only.")
        else:
            result = swap_nodes(input_linked_list.head, k[i])
            print("\tLinked list with swapped values: ", end="")
            print_list_with_forward_arrow(result)
        print("\n", "-" * 100, sep="")


if __name__ == '__main__':
    main()

# Time complexity
# The time complexity of this solution is O(n), where nis the number of nodes in the linked list.
#
# Space complexity
# The space complexity of the solution is O(1).
