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

    queue.append((click[0], click[1]))
    board[click[0]][click[1]] = reveal_board[click[0]][click[1]]
    visitsed = [[False for _ in range(n)] for _ in range(m)]
    
    while queue:

        x, y = queue.popleft()
        # 지뢰를 탐색하려고 하면 바로 종료
        if board[x][y] == "M":
            continue
        if board[x][y] == "B":
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < m and 0 <= ny < n:
                    board[nx][ny] = reveal_board[nx][ny]
                    # 8방향을 탐색하는데 방문 안했고 빈공간이면 queue에 넣는다
                    if reveal_board[nx][ny] == "B" and visitsed[nx][ny] is False:
                        visitsed[nx][ny] = True
                        queue.append((nx, ny))
    return(board)


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]



updateBoard(board, click)
