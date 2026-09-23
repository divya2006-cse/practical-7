
def coin_change(N, coins):
    m = len(coins)
    dp = [[0] * (N + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, N + 1):

            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]

            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

    return dp[m][N]


N = int(input("Enter N: "))
coins = list(map(int, input("Enter coins: ").split()))
print("Number of ways:", coin_change(N, coins))
