def permutation(arr, visited, per, depth):
    if depth == len(arr):
        yield tuple(per)  # 순열을 생성할 때마다 tuple로 변환하여 반환
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            per.append(arr[i])
            yield from permutation(arr, visited, per, depth + 1)
            per.pop()
            visited[i] = False

def solution():
    arr = [1, 2, 3]
    visited = [False] * len(arr)
    for perm in permutation(arr, visited, [], 0):
        print(perm)

solution()