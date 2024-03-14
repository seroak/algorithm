n = int(input())
arr = list(map(int, input().split()))
visit = [False for _ in range(n)]
tmp = list()
per = list()
def dfs(cur, depth):
    if depth == cur:
        per.append(tmp[:])
        return
    for i in range(n):
        if visit[i] is False:
            tmp.append(arr[i])
            visit[i] = True
            dfs(cur + 1, depth)
            visit[i] = False
            tmp.pop()
    return

dfs(0, n)

mx = 0
for i in per:
    num = 0
    for j in range(len(i)-1):
        num += abs(i[j] - i[j+1])
    mx = max(mx, num)
print(mx)

