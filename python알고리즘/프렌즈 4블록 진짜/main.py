m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
def solution(m, n, board):
    answer = 0
    cnt = 0
    for i in range(m):
        board[i] = list(board[i])

    rm = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i][j] == board[i+1][j] and board[i][j] == board[i + 1][j + 1] and board[i][j] == board[i][j+1]:
                    rm.add((i,j))
                    rm.add((i+1, j))
                    rm.add((i+1, j+1))
                    rm.add((i, j+1))

        if rm:
            cnt += len(rm)
            for i, j in rm:
                board[i][j] = []
            rm = set()
        else:
            break

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] != [] and board[i+1][j] == []:
                    nx = i
                    ny = j

                    while not board[nx + 1][ny]:
                        if nx + 1 == m-1:
                            nx += 1
                            break
                        nx += 1
                    board[nx][ny] = board[i][j]
                    board[i][j] = []



    return cnt
solution(m, n, board)