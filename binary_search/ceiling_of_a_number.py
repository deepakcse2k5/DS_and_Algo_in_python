arr = [1, 3, 8, 10, 15]
key = 12


def ceiling_of_a_number(arr, key):
    low = 0
    high = len(arr) - 1

    if key > arr[high]:
        return -1

    while low <= high:
        mid = (low + high) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            return mid
    return low


# print(ceiling_of_a_number(arr, key))


def floor_of_a_given_number(arr,key):
    low = 0
    high = len(arr)-1
    # if key>arr[high] or key<arr[low]:
    #     return -1
    while low<=high:
        mid = (low+high)//2
        if key<arr[mid]:
            high = mid-1
        elif key>arr[mid]:
            low = mid+1
        else:
            return mid
    return high


# print(floor_of_a_given_number(arr, key))


print(floor_of_a_given_number([4, 6, 10], 6))
print(floor_of_a_given_number([1, 3, 8, 10, 15], 12))
print(floor_of_a_given_number([4, 6, 10], 17))
print(floor_of_a_given_number([4, 6, 10], -1))

