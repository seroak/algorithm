def solution(n, t, m, p):
    answer = ''
    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]
    answer = ""
    cadidate = []
    for i in range(t*m):
    return answer
