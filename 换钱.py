
def coinChange(amount,coins=[1,2,5]):
    dp = [0] + [float('inf')]*amount
    #相当于存储的最优解
    for coin in coins[::-1]:
    #分别用不同面值的硬币去尝试自底向顶构建最优解
        for x in range(coin,amount+1):
            #用不同同币值去构建
            dp[x] = min(dp[x] ,dp[x-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1
print(coinChange(11))

