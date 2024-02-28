n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
sum_a = list()
sum_b = list()
for i in range(n):
    for j in range(n):
        sum_a.append(board[i][0] + board[j][1])
        sum_b.append(board[i][2] + board[j][3])

sum_b.sort()
answer = 0
def lower_bound(target):
    st = 0
    en = (n*n) - 1

    while st < en:
        mid = (st + en) // 2
        if target <= sum_b[mid]:
            en = mid
        else:
            st = mid + 1
    return en
def upper_bound(target):
    st = 0
    en = (n*n) - 1

    while st < en:
        mid = (st + en) // 2
        if target < sum_b[mid]:
            en = mid
        else:
            st = mid + 1
    return en
for num in sum_a:
    up_idx = upper_bound((-num))
    low_idx = lower_bound((-num))
    answer += up_idx-low_idx

print(answer)