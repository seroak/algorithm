from collections import deque
def updateBoard(board, click):
    n = len(board[0])
    m = len(board)
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board
    reveal_board = [["B" for _ in range(n)] for _ in range(m)]

    # reveal_board 하나하나씩 확인하면서 폭탄확인하는 숫자 보드로 바꾸기
    for x in range(m):
        for y in range(n):
            if board[x][y] == "M":
                reveal_board[x][y] = "M"
                continue
            count = 0
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "M":
                    count += 1
            if count == 0:
                continue
            reveal_board[x][y] = str(count)


    queue = deque()
    for i in range(8):
        nx = click[0] + dx[i]
        ny = click[1] + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            queue.append((nx, ny))
    board[click[0]][click[1]] = reveal_board[click[0]][click[1]]
    visitsed = [[False for _ in range(n)] for _ in range(m)]
    # 먼저 넘어가서 8방향으로 탐색을 한다
    while queue:

        x, y = queue.popleft()
        # 지뢰를 탐색하려고 하면 바로 종료
        if board[x][y] == "M":
            continue
        flag = False
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            # 8방향을 탐색했는데 빈공간이 있으면 재귀적 탐색이 일어나므로 board 값을 변화 시킨다
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "B":
                # 8방향중 빈공간이 있으므로 B또는 숫자로 바꾼다
                board[x][y] = reveal_board[x][y]
                flag = True
        if flag is True:
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < m and 0 <= ny < n and visitsed[nx][ny] is False:
                    visitsed[nx][ny] = True
                    queue.append((nx, ny))
    old_board = []
    while board != old_board:
        old_board = [arr[:] for arr in board]
        for x in range(m):
            for y in range(n):
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "B":
                        board[x][y] = reveal_board[x][y]
    print(board)


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]



updateBoard(board, click)
