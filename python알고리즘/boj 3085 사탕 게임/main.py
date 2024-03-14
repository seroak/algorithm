n = int(input())
board = [list(map(str, input().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def count_candy():
    row_cnt, col_cnt, row_max, col_max = 1, 1, -1e9, -1e9
    for i in range(n):
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1
    for j in range(n):
        for i in range(n-1):
            if board[i][j] == board[i+1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        col_cnt = 1
    answer = max(row_max, col_max)
    return answer

ans = 0
for i in range(n):
    for j in range(n-1):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
            ans = max(ans, count_candy())
            board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
print(ans)