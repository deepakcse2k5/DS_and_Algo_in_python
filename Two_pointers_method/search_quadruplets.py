# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.

# Time complexity 

# Sorting the array will take O(N∗logN). Overall searchQuadruplets() will take O(N * logN + N^3), which is asymptotically equivalent to O(N^3).
# Space complexity 

# The space complexity of the above algorithm will be O(N) which is required for sorting.



arr = [4, 1, 2, -1, 1, -3]
target=1

def search_quadruplets(arr,target):
    quadruplets = []
    arr.sort()
    
    for i in range(len(arr)-3):
        # skipping duplicate value
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,len(arr)-2):
            if j>0 and arr[j]==arr[j-1]:
                continue
            search_pair(arr,target,i,j,quadruplets)
    return quadruplets

def search_pair(arr,target_sum,first,second,quadruplets):
    left = second+1
    right = len(arr)-1
    while (left<right):
        quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if quad_sum == target_sum:
            quadruplets.append([arr[first],arr[second],arr[left],arr[right]])
            left +=1
            right -=1
            while(left <right and arr[left]==arr[left]-1):
                left+=1
            while (left<right and arr[right]==arr[right]-1):
                right-=1
        elif quad_sum < target_sum:
            left+=1
        else:
            right-=1
            
            
print(search_quadruplets(arr,target))
                
    
    
    