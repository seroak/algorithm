
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dAlpha = ['d', 'l', 'r', 'u']
answer = "z"

n = 3
m = 4
x = 2
y = 3
r = 3
c = 1
k = 5

# 범위를 벗어나지 않는지 확인
def isVaild(nx, ny, n, m):
    return 1 <= nx and nx <= n and 1 <= ny and ny <= m


def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):
        return
    if x == r and y == c and cnt == k:
        answer = prev_s
        return
    for i in range(4):
        if isVaild(x + dx[i], y + dy[i], n, m) and prev_s < answer:
            dfs(n, m, x + dx[i], y + dy[i], r, c, prev_s + dAlpha[i], cnt + 1, k)



def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    dfs(n, m, x, y, r, c, "", 0, k)
    print(answer)
    return answer
solution(n, m, x, y, r, c, k)

