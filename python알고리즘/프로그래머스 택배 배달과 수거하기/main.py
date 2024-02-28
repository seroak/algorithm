cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_idx = n-1
    pickup_idx = n-1
    while deliver_idx >= 0 and deliveries[deliver_idx] == 0:
        deliver_idx -= 1
    while pickup_idx >= 0 and pickups[pickup_idx] == 0:
        pickup_idx -= 1

    while pickup_idx >= 0 or deliver_idx >= 0:

        while deliver_idx >= 0 and deliveries[deliver_idx] == 0:
            deliver_idx -= 1
        while pickup_idx >= 0 and pickups[pickup_idx] == 0:
            pickup_idx -= 1
        answer += 2*max(deliver_idx+1, pickup_idx+1)
        # 배달을 하는 로직
        tmp_cap = cap
        # 한번에 할 수 있는 배달을 다 하거나 더이상 배달을 할 수 있는 곳이 없을 때까지 반복
        while tmp_cap > 0 and deliver_idx >= 0:
            # 배달을 처음 칸에서 다 할 수 있는 경우
            if deliveries[deliver_idx] >= tmp_cap:
                deliveries[deliver_idx] -= tmp_cap
                tmp_cap = 0
            else:
                # 배달을 처음 칸에서 다 할 수 없을 때
                while deliver_idx >= 0 and tmp_cap > 0:
                    # tmp_cap이 남을때
                    if tmp_cap - deliveries[deliver_idx] >= 0:
                        # 배달가능한 물건이 남을 때
                        tmp_cap -= deliveries[deliver_idx]
                        deliveries[deliver_idx] = 0
                        deliver_idx -= 1
                    # tmp_cap이 안남을때
                    else:
                        # 배달가능한 물건을 다 소진했을 때
                        deliveries[deliver_idx] -= tmp_cap
                        tmp_cap = 0


        # 수거를 하는 로직
        tmp_cap = cap
        # 한번에 할 수 있는 수거를 다 하거나 더이상 수거할 수 있는 곳이 없을 때까지 반복
        while tmp_cap > 0 and pickup_idx >= 0:
            # 처음만난 칸에서 다 수거가 가능할때
            if pickups[pickup_idx] >= tmp_cap:
                pickups[pickup_idx] -= tmp_cap
                tmp_cap = 0
            else:
                while tmp_cap > 0 and pickup_idx >= 0:
                    # 이번칸에서 다 수거가 불가능할 때
                    if tmp_cap - pickups[pickup_idx] >= 0:
                        tmp_cap -= pickups[pickup_idx]
                        pickups[pickup_idx] = 0
                        pickup_idx -=1
                    else:
                        pickups[pickup_idx] -= tmp_cap
                        tmp_cap = 0

    return answer
# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     # i는 배달 인덱스 j는 픽업 인덱스
#     i = n - 1
#     j = n - 1
#     # 가장 먼 택배 배달 위치를 구하는 로직
#     while i >= 0 and deliveries[i] == 0:
#         i -= 1
#     # 가장 먼 택배 픽업 위치를 구하는 로직
#     while j >= 0 and pickups[j] == 0:
#         j -= 1
#
#     while i >= 0 or j >= 0:
#         while i >= 0 and deliveries[i] == 0:
#             i -= 1
#         # 가장 먼 택배 픽업 위치를 구하는 로직
#         while j >= 0 and pickups[j] == 0:
#             j -= 1
#         answer += 2 * (max(i, j) + 1)
#         # 가장 먼 배달위치부터 배달을 하는 로직
#         tmp_cap = cap
#         # 현재 배달해야하는 곳이 용량보다 배달 물건이 많을 때
#         if deliveries[i] > tmp_cap:
#             deliveries[i] -= tmp_cap
#         else:
#             # 현재 배달하는 곳이 용량보다 적을 때
#             # 인덱스가 0보다 크거나 같고 배달 가능한 갯수가 0보다 클 때까지 반복
#             while i >= 0 and tmp_cap > 0:
#
#                 if tmp_cap - deliveries[i] >= 0:
#                     # 배달가능한 물건이 남을 때
#                     tmp_cap -= deliveries[i]
#                     deliveries[i] = 0
#                     i -= 1
#                 else:
#                     # 배달가능한 물건을 다 소진했을 때
#                     deliveries[i] -= tmp_cap
#                     tmp_cap = 0
#
#         # 같은 로직의 픽업
#         tmp_cap = cap
#         if pickups[j] > tmp_cap:
#             pickups[j] -= tmp_cap
#         else:
#             while j >= 0 and tmp_cap > 0:
#                 if tmp_cap - pickups[j] >= 0:
#                     tmp_cap -= pickups[j]
#                     pickups[j] = 0
#                     j -= 1
#                 else:
#                     pickups[j] -= tmp_cap
#                     tmp_cap = 0
#
#     return answer
solution(cap, n, deliveries, pickups)