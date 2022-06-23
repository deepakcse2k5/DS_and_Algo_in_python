# Brute Force approach

# input :- Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# output :- [2.2, 2.8, 2.4, 3.6, 2.8]
# Time complexity - O(N*K) where N is the length of array

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]


def find_avg_of_subarray(arr, k):
    if len(arr) < 5:
        return 0
    avg_arr = []
    for i in range(len(arr) - k + 1):
        sum = 0.0
        for j in range(i, i + k):
            sum += arr[j]
        avg_arr.append(sum / k)

    return avg_arr


# Time Compexity - O(N*K) , Space Complexity - O(1)

print(find_avg_of_subarray(arr, k=5))


# sliding window approach

def find_averages_of_subarrays1(K, arr):
    result = []
    start = 0
    sum = 0.0
    for i in range(len(arr)):
        sum += arr[i]
        if i >= K - 1:
            result.append(sum / K)
            sum -= arr[start]
            start += 1
    return result


print(find_averages_of_subarrays1(5, arr))

# Time Compexity - O(N) , Space Complexity - O(1)
