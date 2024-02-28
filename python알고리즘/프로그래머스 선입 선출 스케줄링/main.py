n = 12
cores = [1, 2, 3, 4]


def solution(n, cores):
    answer = 0
    # 코어의 길이보다 작거나 같으면 바로 n을 리턴
    if n <= len(cores):
        return n
    else:
        n -= len(cores)
        left = 1
        # 가장 오래 걸리는 코어의 시간 * n
        # cores에 core가 하나이고 1이라면 지금 나오는 right가 정답인 상황이다 즉 최대값
        right = max(cores) * n

        while left < right:
            # mid는 이 시간까지 했을 때 할당량 보다 적은데 가장 큰 경우를 찾는다
            mid = (left + right) // 2
            capacity = 0
            for c in cores:
                # 각각의 코어의 약수를 capacity에 더한다
                capacity += mid // c
            if capacity >= n:
                right = mid
            else:
                left = mid + 1

        for c in cores:
            n -= (right-1) // c
        for i in range(len(cores)):
            if right % cores[i] == 0:
                n -= 1
            if n == 0:
                answer = (i+1)
                break



    return answer


solution(n, cores)
