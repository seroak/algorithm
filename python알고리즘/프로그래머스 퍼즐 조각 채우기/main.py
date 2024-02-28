from collections import deque
game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
def find_block(board, f):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    n = len(board)
    visited = [[False for _ in range(n)]for _ in range(n)]
    result = list()
    for i in range(n):
        for j in range(n):
            if board[i][j] == f and visited[i][j] is False:
                tmp = deque()
                tmp.append((i, j))
                visited[i][j] = True
                dist = list()

                while tmp:
                    x, y = tmp.popleft()
                    dist.append((x, y))
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] is False and board[nx][ny] == f:
                            tmp.append((nx, ny))
                            visited[nx][ny] = True
                result.append(dist)

    return result
def make_table(block):
    x, y = zip(*block)
    c, r = max(x) - min(x) + 1, max(y) - min(y) + 1
    table = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(len(x)):
        table[x[i] - min(x)][y[i] - min(y)] = 1
def rotate(puzzle_block):
    x, y = len(puzzle_block), len(puzzle_block[0])
    count = 0
    tmp = [[0 for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if puzzle_block[i][j] == 1:
                count += 1
            tmp[j][x-1-i] = puzzle_block[i][j]
    return tmp, count
def solution(game_board, table):
    answer = -1
    empty_block = find_block(game_board, 0)
    puzzles = find_block(table, 1)
    print(empty_block)
    print(puzzles)
    for empty in empty_block:
        filled = False
        table = make_table(empty)
        for puzzle in puzzles:
            puzzle_block = make_table(puzzle)
            for _ in range(4):
                puzzle, count = rotate(puzzle_block)

    return answer
solution(game_board, table)