lst = [4,2,-5,1,2,3,6,-8,9]
def  find_max_sum_sublist(lst):
    if len(lst)<1:
        return 0
    curr_max=lst[0]
    global_max = lst[0]
    
    for i in range(1,len(lst)):
        if curr_max <0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
    if global_max < curr_max:
        global_max=curr_max
        
    return global_max


print(find_max_sum_sublist(lst))
    