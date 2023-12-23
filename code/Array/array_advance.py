def arr_advance(arr):
    i =0
    last_idx = len(arr)-1
    furthest_reach =0
    while i<= furthest_reach and furthest_reach<=last_idx:
        furthest_reach = max(furthest_reach,arr[i]+i)
        i+=1
    return furthest_reach>=last_idx

A = [3,2,0,0,2,0,1]
print(arr_advance(A))


A = [3, 3, 1, 0, 2, 0, 1]

print(arr_advance(A))