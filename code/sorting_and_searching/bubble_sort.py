arr = [8, 5, 4, 3, 7, 9, 1, 6, 2]


# Time Complexity - O(N^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort1(arr):
    n = len(arr)

    for i in reversed(range(n)):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
        return arr


print(bubble_sort(arr))

print(bubble_sort1(arr))
