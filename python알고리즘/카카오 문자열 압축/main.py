s = "aabbaccc"
def solution(s):
    result = []
    if len(s) == 1:
        return 1
    # 반이 넘어버리면 그 이상의 문자열 압축은 의미가 없으므로
    for i in range(1, len(s)//2 + 1):
        print(i)
        cnt = 1
        b = ""
        # 나누는 기준이 되는 변수
        tmp = s[:i]
        for j in range(i, len(s), i):
            print(j)
            if tmp == s[j: i+j]:
                cnt += 1
            else:
                if cnt == 1:
                    b += tmp
                else:
                    b += str(cnt) + tmp

                tmp = s[j: i+j]
                cnt = 1
        if cnt != 1:
            b += str(cnt) + tmp
        else:
            b = b + tmp
        result.append(len(b))
    return min(result)
solution(s)