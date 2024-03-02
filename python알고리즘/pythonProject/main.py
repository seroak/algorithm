from collections import deque
import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dist = dict()
start = ''
for i in range(3):
    a = str(input())
    a = a.replace(' ','')
    start += a

start = start.replace('0','9')
print(start)
dist[start] = 0
def bfs():
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if x == "123456789":
            return dist[x]
        s = x
        k = s.find('9')
        a, b = k//3, k%3
        for i in range(4):
            na = dx[i] + a
            nb = dy[i] + b
            if 0 <= na < 3 and 0 <= nb < 3:
                # 1차원 배열에서의 위치
                nk = na*3 + nb
                ns = list(x)
                ns[k], ns[nk] = ns[nk], ns[k]
                nx = str(''.join(ns))
                # 같은 퍼즐 배열이 나오면 거른다
                if not dist.get(nx):
                    dist[nx] = dist[x] + 1
                    queue.append(nx)
    return
print(bfs())