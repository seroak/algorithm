from collections import deque
import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i, j)
            if board[i][j] == "G":
                dest = (i, j)
    dist = [[sys.maxsize for _ in range(m)] for _ in range(n)]
    queue = deque()
    dist[start[0]][start[1]] = 0
    queue.append((start[0], start[1], 0))
    while queue:
        x, y, cost = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 벽에 부딪치거나 끝에 닿았을 때 종료
            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if board[nx][ny] == "D":
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                nx += dx[i]
                ny += dy[i]

            # 탐색한 경로가 더 짧을 때 dist에 갱신
            if dist[nx][ny] > cost + 1:

                dist[nx][ny] = cost + 1
                queue.append((nx, ny, cost + 1))

    answer = dist[dest[0]][dest[1]]
    return answer
solution(board)