n = 15
def solution(n):
    answer = 0
    arr = list()
    n_sum = 0
    arr.append(0)
    for i in range(1, n+1):
        n_sum += i
        arr.append(n_sum)

    left = 0
    right = 1
    while left < right:
        # 누적합이 목표치보다 적을 때
        if arr[right] - arr[left] < n:
            right += 1
        # 누적합이 목표치보다 많을 때
        elif arr[right] - arr[left] > n:
            left += 1
        else:
            answer += 1
            left += 1

    return answer
solution(n)