from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

def solution(m, n, board):
    answer = 0
    flag = True
    # flag가 False면 종료 4개이상이 없다는 뜻
    while flag:
        flag = False
        visited = [[False for _ in range(n)] for _ in range(m)]
        rm = list()
        for i in range(m):
            for j in range(n):
                if visited[i][j] is False:
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True
                    rm_tmp = list()
                    cnt = 0
                    while queue:
                        cnt += 1
                        x, y = queue.popleft()
                        rm_tmp.append((x, y))

                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            # 범위를 벗어나지 않고 처음에 들어왔던 곳과 값이 같으면 queue에 넣는다
                            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == board[i][j] and visited[nx][ny] is False:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                    if cnt >= 4:
                        rm.append(rm_tmp[:])
        print(visited)
        print(rm)
    return answer
solution(m, n, board)