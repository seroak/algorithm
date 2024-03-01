picks = [1,3,2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
def solution(picks, minerals):
    sum = 0
    for x in picks:
        sum += x
    # 캘 수 있는 광물의 개수
    num_min = sum * 5
    if len(minerals) > num_min:
        # 캘 수 있는 광물의 캘 수 있는 광물 보다 많으면 짜른다
        minerals = minerals[:num_min]

    # 광물 조사
    # 광물을 5개씩 묶고 광물의 길이는 최대 50개이므로 10개의 배열을 만든다
    cnt_min = [[0, 0, 0] for x in range(10)] # dia, iron, stone
    # 5개씩 묶은 광물의 종류를 배열에 저장한다
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            cnt_min[i//5][0] += 1
        elif minerals[i] == "iron":
            cnt_min[i//5][1] += 1
        else:
            cnt_min[i//5][2] += 1

    # 피로도가 높은 순서대로 광물 정렬
    # 광물은 정렬을 하지 못하지만 곡괭이는 정렬을 할 수 있다 즉 광물을 정렬하고 곡괭이를 정렬을 안하면 곡괭이만 정렬한것과 같다
    # 다이아 곡괭이 부터 for문으로 처리하기 때문에 피로도가 높은 순으로 정렬하면 가장 최적의 경우를 따질 수 있다
    sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))

    # 곡괭이 수

    # 피로도 계산
    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        # picks 길이 만큼 반복
        for p in range(len(picks)):
            # 다이아 곡괭이 일때 다이아 곡괭이가 0이 아닐 때
            # if 문 안으로 들어가면 break으로 빠져나온다
            if p == 0 and picks[p] > 0:
                picks[p] -= 1
                answer += d + i + s
                break
            elif p == 1 and picks[p] > 0:
                picks[p] -=1
                answer += 5 *d + i + s
                break
            elif p == 2 and picks[p] > 0:
                picks[p] -= 1
                answer += 25*d + 5*i + s
                break
    print(answer)
    return answer
solution(picks, minerals)