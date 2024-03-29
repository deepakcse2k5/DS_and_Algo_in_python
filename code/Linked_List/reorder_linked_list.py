from linked_list import LinkedList
from print_list import print_list_with_forward_arrow


def reorder_list(head):
    if not head:
        return head
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, curr = None, slow

    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    first, second = head, prev

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head


def main():
    input_list = [
        [1, 1, 2, 2, 3, -1, 10, 12],
        [10, 20, -22, 21, -12],
        [1, 1, 1],
        [-2, -5, -6, 0, -1, -4],
        [3, 1, 5, 7, -4, -2, -1, -6]
    ]

    for i, inp in enumerate(input_list):
        obj = LinkedList()
        obj.create_linked_list(inp)

        print(i + 1, ".\tOriginal list: ", end="", sep="")
        print_list_with_forward_arrow(obj.head)

        obj.head = reorder_list(obj.head)

        print("\n\tAfter folding: ", end="")
        print_list_with_forward_arrow(obj.head)
        if i != len(input_list) - 1:
            print("\n", "-" * 100, sep="")


if __name__ == '__main__':
    main()