from itertools import permutations

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak]

    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            # 처음 시작 위치
            position = start
            # 친구 조합 배치
            for friend in friends:
                # 친구를 추가 배치한 후 있는 위치
                position += friend
                # 끝 포인트에 도달 못했을 때
                if position < weak_point[i+L-1]:
                    count += 1
                    position = [w for w in weak_point[i + 1:i + L]if w > position][0]
                else:
                    cand.append(count)
                    break
    return min(cand) if cand else -1

solution(n, weak, dist)