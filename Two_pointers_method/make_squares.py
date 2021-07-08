# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Time and Space complexity is O(N) because we are iterating input and output array only once

arr = [-2, -1, 0, 2, 3]

def make_squares(arr):
    start = 0
    end = len(arr)-1
    squares = [0 for x in range(len(arr))]
    highest_square_index = len(arr)-1
    
    while start<=end:
        startsquare = arr[start] * arr[start]
        endsquare = arr[end] * arr[end]
        
        if startsquare > endsquare:
            squares[highest_square_index] = startsquare
            start+=1
        else:
            squares[highest_square_index] = endsquare
            end -=1
        highest_square_index -=1
    return squares


print(make_squares(arr))
            
        