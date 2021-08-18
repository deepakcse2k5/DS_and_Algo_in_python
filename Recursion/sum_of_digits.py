def sum_of_digits(n):
    assert n>=0 and int(n)==n , "number should be positive integer"
    if n==0:
        return 0
    if (n>0):
        return n%10 + sum_of_digits(n//10)
        
        
print(sum_of_digits(23456))
            
            