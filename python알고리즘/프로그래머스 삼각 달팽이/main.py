n = 1
def solution(n):
    answer = []
    tri = list()
    for i in range(n):
        tmp = [0 for _ in range(i+1)]
        tri.append(tmp)
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x = 0
    y = 0
    # 네모 칸을 체우는 숫자
    num = 1
    # 방향을 결정하는 숫자
    cnt = 0
    if n == 1:
        answer.append(1)
        return answer
    while True:
        # 다음에 방문해야할 곳이 이미 방문 한 곳이면  while문을 종료

        if tri[x][y] != 0:
            break
        while True:
            # 세모칸의 범위를 벗어나면 while문 종료
            if x < 0 or x >= n or y < 0 or y >= n:
                x -= dx[cnt]
                y -= dy[cnt]
                break
            # 이전에 방문한곳에 다시 들어가면 while문 종료
            if tri[x][y] != 0:

                x -= dx[cnt]
                y -= dy[cnt]
                break

            tri[x][y] = num
            x += dx[cnt]
            y += dy[cnt]
            num += 1
        cnt = (cnt + 1) % 3
        x += dx[cnt]
        y += dy[cnt]

    for tmp in tri:
        answer.extend(tmp)
    print(answer)
    return answer
solution(n)