arr = [8,5,4,3,7,9,1,6,2]

# Time Complexity - O(N^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    return arr



print(bubble_sort(arr))
                
                