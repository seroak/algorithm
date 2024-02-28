from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    queue = deque()
    visited = [False for _ in range(n)]
    for j in range(n):
        if graph[i][j] == 1:
            queue.append(j)
            visited[j] = True
            answer[i][j] = 1

    while queue:
        cur = queue.popleft()
        for idx in range(len(graph[cur])):
            if graph[cur][idx] == 1:
                if visited[idx] is False:
                    queue.append(idx)
                    visited[idx] = True
                    answer[i][idx] = 1

for i in answer:
    print(*i)