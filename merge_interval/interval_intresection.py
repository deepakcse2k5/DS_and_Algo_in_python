# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.


# Time complexity - O(N+M) where N and M is the length of arrays. Space Complexity - O(1)



def intersect_interval(arr1,arr2):
    result = []
    
    i,j,start,end = 0,0,0,1
    
    while i<len(arr1) and j<len(arr2):
        # check if intervals overlap and arr1's start time lies within the other arr2
        arr1_overlaps_arr2 = arr1[i][start] >= arr2[j][start] and arr1[i][start] <= arr2[j][end]
        
        
        # check if intervals overlap and arr2's start time lies within the other arr1
        
        arr2_overlaps_arr1 = arr2[j][start] >=arr1[i][start] and arr2[j][start] <= arr1[i][end]
        
        # store interval intersection
        
        if (arr1_overlaps_arr2 or arr2_overlaps_arr1):
            result.append([max(arr1[i][start],arr2[j][start]) , min(arr1[i][end],arr2[j][end])])
            
        # move next interval which is going to finish first
        
        if arr1[i][end] <= arr2[j][end]:
            i+=1
        else:
            j+=1
    return result


def main():
    print("Intervals Intersection: " + str(intersect_interval([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(intersect_interval([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
        
        
        
    