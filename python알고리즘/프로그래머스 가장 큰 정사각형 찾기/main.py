from collections import deque

dx = [0, 1, 1]
dy = [1, 1, 0]
board = [[0,0,1,1],[1,1,1,1]]

def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            
            if board[i][j] == 1:
                queue = deque()
                queue.append((i, j, 1))
                while queue:
                    x, y, level = queue.popleft()
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 1:
                        for k in range(3):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            queue.append((nx, ny, level + 1))
                    else:
                        answer = max(answer, level)
                        break

    print(answer)
    return answer
solution(board)