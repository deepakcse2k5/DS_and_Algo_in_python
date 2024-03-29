from linked_list import LinkedList
from print_list import print_list_with_forward_arrow


def reverse_even_length_groups(head):
    prev = head
    l = 2

    while prev.next:
        node = prev
        n = 0
        for i in range(l):
            if not node.next:
                break
            n += 1
            node = node.next
        if n % 2:
            prev = node
        else:
            reverse = node.next
            curr = prev.next
            for j in range(n):
                curr_next = curr.next
                curr.next = reverse
                reverse = curr
                curr = curr_next
            prev_next = prev.next
            prev.next = node
            prev = prev_next
        l += 1

    return head


# Driver Code

def to_list(head):
    lst = []
    temp = head
    while temp:
        lst.append(temp.data)
        temp = temp.next
    return lst


def main():
    input = [
        [1, 2, 3, 4],
        [10, 11, 12, 13, 14],
        [15],
        [16, 17]
    ]

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(
            i+1, ".\tIf we reverse the even length groups of the linked list: ", end='\n\t', sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\n\tWe will get: ", end='\n\t')
        print_list_with_forward_arrow(
            reverse_even_length_groups(input_linked_list.head))
        print("\n", "-" * 100)


if __name__ == '__main__':
    main()


# Time complexity
# The time complexity will be O(n), since we traverse the n nodes of the linked list.
#
# Space complexity
# The space complexity will be O(1), since we use a constant number of additional variables to maintain the proper connections between the nodes during reversal.