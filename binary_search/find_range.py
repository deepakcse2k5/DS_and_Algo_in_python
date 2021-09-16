arr = [4, 6, 6, 6, 6, 9]
key = 6


def find_range(arr, key):
    start = 0
    end = len(arr) - 1
    key_range = []
    # edge case
    if key < arr[start] or key > arr[end]:
        return [-1, -1]
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            key_range.append(mid)
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return key_range[0], key_range[-1]


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
