arr = [1, 2, 3, 4, 5, 6, 7]
key = 5


def binary_search(arr, key):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1

    while low<=high:
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid+1
    return -1


print(binary_search(arr, 3))
