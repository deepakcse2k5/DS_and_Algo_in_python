# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Sorting the array will take O(N∗logN). 
# The searchPair() function will take O(N). 
# As we are calling searchPair() for every number in the input array, 
# this means that overall searchTriplets() will take O(N * logN + N^2),
# which is asymptotically equivalent to O(N2)O(N^2)O(N​2​​).
# Space complexity will be O(N^2) which is required for sorting the  input array


arr = [-3, 0, 1, 2, -1, 1, -2]

def search_triplets(arr):
    arr.sort()
    triplets = []
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        if i>0 and arr[i]==arr[i-1]:
            continue
        search_pair(arr,-arr[i],i+1,triplets)
    return triplets

def search_pair(arr,target_sum,left,triplets):
    right = len(arr)-1
    while left<right:
        curr_sum = arr[left] + arr[right]
        if curr_sum==target_sum:
            triplets.append([-target_sum,arr[left],arr[right]])
            left+=1
            right-=1
            while left<right and arr[left] == arr[left]-1:
                left+=1
            while left<right and arr[right] == arr[right]-1:
                right -=1
        elif target_sum > curr_sum:
            left +=1
        else:
            right -=1
            
        
            
    
    

print(search_triplets(arr))