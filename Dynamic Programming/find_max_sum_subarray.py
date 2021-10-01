arr = [-4, 2, -5, 1, 2, 3, 6, -5, 1]


def find_max_sum_sub_array(arr):
    if len(arr) < 1:
        return 0

    curr_max = 0
    global_max = 0

    for i in range(len(arr)):
        if curr_max < 0:
            curr_max = arr[i]
        else:
            curr_max += arr[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max


print(find_max_sum_sub_array(arr))
