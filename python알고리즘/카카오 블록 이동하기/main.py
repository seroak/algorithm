from collections import deque
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
def can_move(cur1, cur2, new_board):
    Y, X = 0, 1
    cand = []
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    # 평행이동
    for i in range(4):
        cand.append([((cur1[0] + dx[i], cur1[1] + dy[i]), (cur2[0] + dx[i], cur2[1] + dy[i]))])
    # 세로 일때 가로로 회전
    if cur1[1] == cur2[1]:
        cand.append([((cur1[0], cur1[1]), (cur1[0], cur1[1]+1))])
        cand.append([((cur2[0], cur2[1]-1), (cur2[0], cur2[1]))])
def solution(board):
    answer = 0
    N = len(board)
    new_board = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])
    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in confirm:
    return answer
solution(board)