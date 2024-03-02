import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    ret = 10001
    q = deque([(0, 0)])
    visit[0][0] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == n - 1 and ny == m - 1:
                return min(ret, visit[x][y] + 1)

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

            elif graph[nx][ny] == 2 and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                ret = min(ret, visit[nx][ny] + abs(n - 1 - nx) + abs(m - 1 - ny))

    return ret


n, m, t = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
visit = [[0] * m for i in range(n)]

ans = bfs()
for i in visit:
    print(i)

print("Fail" if ans > t else ans)