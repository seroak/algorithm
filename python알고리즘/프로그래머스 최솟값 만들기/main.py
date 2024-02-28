import sys
from itertools import permutations
A = [1, 4, 2]
B = [5, 4, 4]
def solution(A, B):
    answer = 0
    mn = sys.maxsize
    A.sort()
    B.sort(reverse=True)

    result = 0
    for i in range(len(A)):
        result += (B[i] * A[i])
    mn = min(result, mn)
    print(mn)
    return answer
solution(A, B)