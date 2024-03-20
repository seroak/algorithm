import sys

sys.setrecursionlimit(10**9)
n, m = map(int, input().split())
graph = [[]for _ in range(n)]
visit = [False for _ in range(n)]
flag = False
def dfs(cur, depth):
    global flag
    if depth == 5:
        flag = 1
        return
    for nxt in graph[cur]:
        if visit[nxt] is False:
            visit[nxt] = True
            dfs(nxt, depth+1)
            visit[nxt] = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    visit[i] = True
    dfs(i, 1)
    if flag:
        break
    visit[i] = False
if flag:
    print(1)
else:
    print(0)