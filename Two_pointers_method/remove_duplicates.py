# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Time complexity O(N) and Space Complexity O(1)

arr = [2,3,3,3,6,9,9]

def renove_duplicates(arr):
    next_non_duplicate =1
    
    i =1
    while (i < len(arr)):
        if arr[next_non_duplicate-1]!=arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate+=1
        i+=1
        
    return next_non_duplicate


print(renove_duplicates(arr))
            