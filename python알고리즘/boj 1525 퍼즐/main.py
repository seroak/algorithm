from collections import deque
import sys

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = dict()
start = ''
for i in range(3):
    a = str(input())
    a = a.replace(' ','')
    start += a

start = start.replace('0','9')

dist[start] = 0

def bfs():
    que = deque()
    que.append(start)
    while que:
        x = que.popleft()

        if x == "123456789":
            return dist[x]
        s = x
        k = s.find('9')
        # 9 가 있는 x값과 y값
        a, b = k//3, k % 3
        for i in range(4):
            na = a + move[i][0]
            nb = b + move[i][1]
            if 0 <= na < 3 and 0 <= nb < 3:
                nk = na*3 + nb
                ns = list(s)
                # 9에서 4방향중 한방향으로 9하고 위치를 바꾼다
                ns[k], ns[nk] = ns[nk], ns[k]
                nx = str(''.join(ns))
                # 같은 퍼즐 배열이 나오면 거른다
                if not dist.get(nx):
                    dist[nx] = dist[x] + 1
                    que.append(nx)


    return -1

print(bfs())

