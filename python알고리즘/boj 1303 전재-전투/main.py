from collections import deque
n, m = map(int,input().split())
board = [list(map(str, input().rstrip()))for _ in range(m)]
visited = [[False for _ in range(n)]for _ in range(m)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
W_num = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] is False and board[i][j] == "W":
            queue = deque()
            visited[i][j] = True
            queue.append((i,j))
            tmp = 0
            while queue:
                x, y = queue.popleft()
                tmp += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] is False and board[nx][ny] == "W":
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            W_num += tmp * tmp
print(W_num, end=" ")

visited = [[False for _ in range(n)]for _ in range(m)]
B_num = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] is False and board[i][j] == "B":
            queue = deque()
            visited[i][j] = True
            queue.append((i,j))
            tmp = 0
            while queue:
                x, y = queue.popleft()
                tmp += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] is False and board[nx][ny] == "B":
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            B_num += tmp * tmp
print(B_num)