# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
# Time complexity O(N) and Space Complexity O(1)

arr = [3,2,3,6,3,10,9,3]
key =3


def remove_element(arr,key):
    next_element =0
    
    for i in range(len(arr)-1):
        if arr[i]!=key:
            arr[next_element]=arr[i]
            next_element+=1
            
    return next_element


print(remove_element(arr,key))
    