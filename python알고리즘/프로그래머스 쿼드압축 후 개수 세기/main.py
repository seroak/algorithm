
def solution(arr):
    answer = [0, 0]
    n = len(arr)
    def quard(x, y, n):
        first = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != first:
                    n //= 2
                    quard(x, y,n)  # 왼쪽 위
                    quard(x, y + n, n) # 오른쪽 위
                    quard(x + n, y, n) # 왼쪽 아래
                    quard(x + n, y + n, n) # 오른쪽 아래
                    return
        answer[first] += 1
    quard(0, 0, n)
    print(answer)
    return answer

solution(arr)