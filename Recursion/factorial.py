def factorial(num):
    
    assert num>0 and int(num)==num, "num must be positive integer only"
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num-1)
    
    
# print(factorial(1.5))
# print(factorial(-1))

print(factorial(5))