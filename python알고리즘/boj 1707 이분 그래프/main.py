import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
k = int(input())

def DFS(start, visited, graph, group):
    visited[start] = group
    for i in graph[start]:
        # 방문을 하지 않았다면
        if visited[i] == 0:
            result = DFS(i, visited, graph, -group)
            if result is False:
                return False
        else:
            if group == visited[i]:
                return False
    return True


for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            result = DFS(i, visited, graph, 1)
            if not result:
                break
    print("YES") if result else print("NO")













