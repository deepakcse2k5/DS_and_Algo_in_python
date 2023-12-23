def recursive_range(num):
    assert num>=0 and int(num)==num,"num should be positive integer only"
    if num in [0,1]:
        return num
    else:
        return num+recursive_range(num-1)
    
    
    
print(recursive_range(6))