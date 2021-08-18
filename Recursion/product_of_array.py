
def productOfArray(arr):
    # assert len(arr)>0 ,"length of array should be greater than 0"
   
    # if 0 in arr:
    #     return 0
    if len(arr)==0:
        return 1
    else:
            
        return arr.pop() * productOfArray(arr)
        
        
print(productOfArray([1,2,3]))

