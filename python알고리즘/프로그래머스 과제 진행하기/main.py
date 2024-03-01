from collections import deque

plans=[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
def solution(plans):
    answer = []
    new_plans = deque()
    for name, start, playtime in plans:
        hour, minute = start.split(":")
        time = int(hour) * 60 + int(minute)
        new_plans.append([time, int(playtime), name])

    new_plans = deque(sorted(new_plans))

    timer = new_plans[0][0]
    working = [new_plans[0]]
    new_plans.popleft()
    sleep = []
    while True:

        # 시간이 증가하고
        timer += 1
        # 진행 중인 과제가 있다면
        if working:
            # 진행 중인 과제의 진행시간이 감소
            working[0][1] -= 1
            # 만약 과제를 다 수행했다면 진행중인 과제에서 제거 후 answer에 넣는다
            if working[0][1] == 0:
                answer.append(working[0][2])
                working.pop()
        # 만약 new_plans가 있을때
        if new_plans:
            # timer가 new_plans의 시작시간이 된다면 진행중인 과제에 새로운 과제를 넣는다
            if timer == new_plans[0][0]:
                # 진행중인 과제가 있다면 잠시 멈춘 과제로 넣는다
                if working:
                    sleep.append(working[0])
                    working.pop()
                working.append(new_plans[0])
                new_plans.popleft()
        # 만약 진행 중인 과제가 없다면 sleep에서 하나를 빼서 넣는다
        if len(working) == 0:
            if sleep:
                working.append(sleep[-1])
                sleep.pop()

        if len(working) == 0 and len(sleep) == 0 and len(new_plans) == 0:
            break

    return answer
solution(plans)