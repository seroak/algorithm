n= 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]
def union(a, b, cost, parent):
    a_parent = find_parent(a, parent)
    b_parent = find_parent(b, parent)
    if a_parent == b_parent:
        return
    if a_parent < b_parent:
        parent[b] = a_parent
    else:
        parent[a] = b_parent
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    print(costs)
    parent = [i for i in range(n)]
    print(parent)
    for a, b, cost in costs:
        union(a, b, cost, parent)
    print(parent)
    return answer
solution(n, costs)