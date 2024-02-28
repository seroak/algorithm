key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate(key):
    x = len(key)  # 열 길이
    y = len(key[0])  # 행 길이
    result = [[0] * y for _ in range(x)]

    for i in range(len(key)):
        for j in range(len(key[0])):
            result[i][j] = key[x - j - 1][i]
    return result


def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n):
        for j in range(n):
            if new_lock[n + i][n + j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True
    n = len(lock)  # 자물쇠 길이
    m = len(key)  # 열쇠 길이
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    new_lock[0][0] = 5

    # 3배 늘린 자물쇠 배열의 중앙에 원래 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    for rot in range(4):
        key = rotate(key)  # 열쇠 회전
        for x in range(2 * n):
            for y in range(2 * n):
                # 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[i + x][j + y] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[i + x][j + y] -= key[i][j]

    return False
solution(key, lock)