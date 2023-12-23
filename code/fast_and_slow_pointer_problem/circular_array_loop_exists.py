# We are given an array containing positive and negative numbers. 
# Suppose the array contains a number ‘M’ at a particular index.
# Now, if ‘M’ is positive we will move forward ‘M’ indices and
# if ‘M’ is negative move backwards ‘M’ indices. You should assume that 
# the array is circular which means two things:

# 1. If, while moving forward, we reach the end of the array, 
# we will jump to the first element to continue the movement.

# 2. If, while moving backward, we reach the beginning of the array, 
# we will jump to the last element to continue the movement.

# Input: [2, 2, -1, 2]
# Output: true
# Explanation: The array has a cycle among indices: 1 -> 3 -> 1

# Input: [2, 1, -1, -2]
# Output: false
# Explanation: The array does not have any cycle.

arr = [2,1,-1,-2]
arr1 = [1, 2, -1, 2, 2]

arr2 =  [2, 2, -1, 2]
def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        slow ,fast= i,i
        while (slow!=fast):
            if fast<0:
                fast = fast - arr[fast]
            else:
                fast = fast - arr[fast]
        if slow==fast:
            return "array has cycle"
    else:
        return "array doesn't have cycle"
    
print(circular_array_loop_exists(arr))


print(circular_array_loop_exists(arr1))

print(circular_array_loop_exists(arr2))
    

            