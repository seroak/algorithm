import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 - 만 사용해서 이동하는 경우
# 이 경우가 가장 많이 이동해야하는 최악의 경우이기 때문에 이것을 min_count에 넣는다
min_count = abs(100 - target)

# 범위를 1000,000으로 하는 이유는 N의 범위가 500,000까지이고
# N이 500,000까지이고 1,2,3,4,5 가 고장났다면
# 100에서 +를 해서 500,000 까지 가는 것이 아니고
# 600,000 에서 -를 해서 500,000까지 가야한다
# 그래서 500,000의 두배인 1000,000 까지 탐색을 한다
for nums in range(1000001):
    # 리모컨으로 누를 수 있는 모든 경우를 for문으로 돌린다
    nums = str(nums)
    for j in range(len(nums)):
        # 공장난 숫자를 사용했다면 break
        if int(nums[j]) in broken:
            break
        # 고장난 숫자 없이 마지막 자리까지 왔다면 mincount 비교 후 업데이트
    else:
        min_count = min(min_count, abs(target - int(nums)) + len(nums))

print(min_count)