# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]
# Time Complexity O(N) and Space Complexity O(1)

arr = [1,0,2,1,0]

def dutch_flag_sort(arr):
    low =0
    high = len(arr)-1
    i =0
    while i<=high:
        if arr[i]==0:
            arr[i],arr[low] = arr[low],arr[i]
            i+=1
            low +=1
        elif arr[i]==1:
            i+=1
        else:
            arr[i],arr[high] = arr[high], arr[i]
            high-=1
    return arr
            
            
print(dutch_flag_sort(arr))
    