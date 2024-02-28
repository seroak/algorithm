n = 4
answer = 0
def solution(n):

    # 직선 배열
    straight = [False for _ in range(n)]
    # 오른쪽 대각선
    r_slash = [False for _ in range((n * 2) - 1)]
    # 왼쪽 대각선
    l_slash = [False for _ in range((n * 2) - 1)]

    def dfs(cur, n):
        global answer
        if cur == n:
            answer += 1

            return
        for i in range(n):
            if straight[i] is False and r_slash[(n-1) + cur - i] is False and l_slash[cur + i] is False:
                straight[i] = True
                r_slash[(n-1) + cur - i] = True
                l_slash[cur + i] = True
                dfs(cur + 1, n)
                straight[i] = False
                r_slash[(n-1) + cur - i] = False
                l_slash[cur + i] = False
        return
    dfs(0, n)
    print(answer)
    return answer
solution(n)