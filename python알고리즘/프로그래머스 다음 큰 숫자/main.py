n = 78
def solution(n):
    answer = 0
    tmp = bin(n)
    binary_n = tmp[2:]
    # 처음 수의 1의 갯수
    count = 0
    for i in binary_n:
        if i == '1':
            count += 1
    print(count)
    while True:
        n += 1
        binary = bin(n)
        binary = binary[2:]
        # 1을 증가시킨 숫자의 이진수의 1을 세는 변수
        one_count = 0
        for i in binary:
            if i == '1':
                one_count += 1
        if one_count == count:
            break
    print(n)
    return answer
solution(n)