
def min_coins(k):
    coins = [1,5,10,25]
    res = []
    n = len(coins)
    i = n-1

    while (i>=0 and k>=0):
        if k>=coins[i]:
            k-=coins[i]
            res.append(coins[i])
        else: i-=1
    return res

print(min_coins(67))
