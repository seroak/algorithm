if __name__ == "__main__":
    N = int(input())
    dy = [0] * (N+1)
    dy[0] = 1
    for i in range(2, N+1):
        dy[i] = dy[i-2] * 3
        for j in range(i-4, -1, -2):
            dy[i] += dy[j] * 2
    dy[0]= 0

    print(dy[N])