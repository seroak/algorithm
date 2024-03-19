n, k = map(int, input().split())
dp = [[0 for _ in range(201)] for _ in range(201)]
for i in range(1, 201):
    dp[0][i] = 1
for i in range(1, 201):
    for j in range(1, 201):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
print(dp[n][k])