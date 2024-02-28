def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def fib_iter(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        prev2 = 0
        prev = 1
        res = 0
        for i in range(1,n):
            res = prev2+prev
            prev2 = prev
            prev = res
        return res 
    
print(fib(10))
print(fib_iter(7))