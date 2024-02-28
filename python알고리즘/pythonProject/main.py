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
print(start)
dist[start] = 0
def bfs():
    que = deque()
    que.append(start)
    while que:
        x = que.popleft()
        if x == "123456789":
            return
        s = x
        k = s.find("9")
        print(k)
        a, b = k//3, k % 3
        for i in range(4):
            na = a + move[i][0]
            nb = b + move[i][1]
            if 0 <= na < 3 and 0 <= nb < 3:
                nk = na*3 + nb
                ns = list(s)
print(bfs())