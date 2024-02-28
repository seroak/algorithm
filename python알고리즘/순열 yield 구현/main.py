def permutations(arr):
    # 재귀적으로 순열을 생성하는 제너레이터 함수
    if len(arr) == 1:
        yield arr
    else:
        for i in range(len(arr)):
            # 현재 요소를 선택하고 나머지 순열을 재귀적으로 생성
            rest_permutations = permutations(arr[:i] + arr[i+1:])
            for rest_permutation in rest_permutations:
                yield [arr[i]] + rest_permutation

# 순열을 생성할 리스트
arr = [1, 2, 3]
print(arr[:1] + arr[1+1:])
# 순열 생성
perm_generator = permutations(arr)

# 순열 출력
for perm in perm_generator:
    print(perm)