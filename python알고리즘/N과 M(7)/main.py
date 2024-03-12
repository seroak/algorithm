n, m = map(int, input().split())
arr = list(map(int, input().split()))
def dfs(cur, depth, arr, comb):
    if cur == depth:
        print(*comb)
        return
    for i in arr:
        comb.append(i)
        dfs(cur+1, depth, arr, comb)
        comb.pop()

arr.sort()
comb = list()
dfs(0, m, arr, comb)