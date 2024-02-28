def permutations(arr):
    result = []
    _permutations(arr, 0, result)
    return result

def _permutations(arr, start, result):
    if start == len(arr) - 1:
        result.append(arr[:])  # 현재 순열을 결과 리스트에 추가
        return

    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]  # 현재 요소를 선택
        _permutations(arr, start + 1, result)  # 나머지 순열 생성
        arr[start], arr[i] = arr[i], arr[start]  # 복구

# 순열을 생성할 리스트
arr = [1, 2, 3]

# 순열 생성
perm_list = permutations(arr)

# 순열 출력
for perm in perm_list:
    print(perm)