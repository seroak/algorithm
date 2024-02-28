import sys
input = sys.stdin.readline

# M 사대의 수,  N 동물의 수, L 사정거리
m, n, l = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

count = 0

for _ in range(n):
    # 동물의 위치
    x, y = map(int, input().split())
    idx = binary_search(s, x)

    dist = abs(x - s[idx]) + y
    dist_left = abs(x - s[idx - 1]) + y if idx > 0 else float('inf')

    dist = min(dist, dist_left)

    if dist <= l:
        count += 1
print(count)