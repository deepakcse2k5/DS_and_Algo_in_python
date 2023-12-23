# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
   
   
   
arr = [-1, 4, 2, 1, 3]

target = 5
def triplet_with_smaller_sum(arr,target):
    arr.sort()
    count =0
    for i in range(len(arr)-2):
        count+=search_pair(arr,target-arr[i],i)
    return count

def search_pair(arr,target_sum,first):
    count =0
    left,right = first+1 , len(arr)-1
    
    while (left < right):
        if (arr[left]+arr[right]<target_sum):
            count+=right-left
            left +=1
        else:
            right -=1
    return count


print(triplet_with_smaller_sum(arr,target))
                
                
                
print(triplet_with_smaller_sum(arr,target))