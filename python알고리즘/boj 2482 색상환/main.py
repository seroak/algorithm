n = int(input())
k = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(1, n+1):
    dp[1][i] = i

if k < 2 or n < 4:
    print(dp[k][n])
else:
    for i in range(2, k+1):
        for j in range(4, n+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j-2]) % 1000000003
    print(dp[k][n])