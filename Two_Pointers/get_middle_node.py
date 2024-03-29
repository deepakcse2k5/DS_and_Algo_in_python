from linked_list import LinkedList
from print_list import *


def get_middle_node(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    input = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i + 1, ".\tLinked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMiddle of the linked list: ",
              get_middle_node(input_linked_list.head).data)
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()

# Time complexity
# The time complexity of this solution is O(n), where n is the number of nodes in the linked list.
# Space complexity
# The space complexity of this solution is O(1), as we are using only a constant amount of space.
