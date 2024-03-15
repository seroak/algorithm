n = int(input())
dp = list(map(int, input().split()))

for i in range(len(dp)):
    st = 0
    en = i - 1
    mn = dp[i]
    while st <= en:
        mn = min(dp[st] + dp[en], mn)
        st += 1
        en -= 1

    dp[i] = mn

print(dp[-1])