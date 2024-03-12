from collections import deque
n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]
cheeze_cnt = 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for i in range(n):
    for j in range(m):
        if 1 == cheeze[i][j]:
            cheeze_cnt += 1
ago_cnt = cheeze_cnt
answer = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m - 1:

                if cheeze[i][j] == 0 and visited[i][j] is False:
                    que = deque()
                    que.append((i, j))
                    while que:
                        x, y = que.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            # 범위를 벗어나지 않고 방문을 한적이 없는 경우
                            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] is False:
                                # 치즈아닌 빈공간일때
                                if cheeze[nx][ny] == 0:
                                    visited[nx][ny] = True
                                    que.append((nx, ny))
                                # 치즈인곳
                                elif cheeze[nx][ny] == 1:
                                    visited[nx][ny] = True
                                    cheeze[nx][ny] = 0
                                    cheeze_cnt -= 1
    answer += 1
    if cheeze_cnt == 0:
        break
    ago_cnt = cheeze_cnt
print(answer)
print(ago_cnt)