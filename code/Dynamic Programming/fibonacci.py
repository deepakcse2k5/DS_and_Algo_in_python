def fib(n):
    dp = [0, 1]
    for i in range(2, n ):
        dp.append(dp[i - 1] + dp[i - 2])
        print(dp)
    return sum(dp)


print(fib(4))
