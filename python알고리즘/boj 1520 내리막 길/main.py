import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]


answer = 0
def dfs(x,y):

    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] < arr[x][y]:

                dp[x][y] = dp[x][y] + dfs(nx, ny)
    return dp[x][y]


answer=dfs(0,0)
print(dp)
print(answer)


