# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
# Time Complexity O(N) and Space Complexity O(1)
arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k=3

def length_of_longest_substring(arr,k):
    start =0
    max_length =0
    num_frequency ={}
    max_repeated_count =0
    for end in range(len(arr)):
        right_num = arr[end]
        if right_num not in num_frequency:
            num_frequency[right_num]=0
        num_frequency[right_num]+=1
        max_repeated_count = max(max_repeated_count,num_frequency[right_num])
        if (end-start+1-max_repeated_count)>k:
            left_num = arr[start]
            num_frequency[left_num]-=1
            start+=1
        max_length = max(max_length,end-start+1)
    return max_length


print(length_of_longest_substring(arr,k))
        