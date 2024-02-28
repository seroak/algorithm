n = int(input())
m = int(input())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
parent = [i for i in range(n+1)]

answer = 0
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True
graph.sort(key=lambda x: x[2])

for a, b, cost in graph:
    if union_parent(parent, a, b):

        answer += cost



print(answer)