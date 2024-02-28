p = "()))((()"
def divide(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        elif p[i] == ")":
            cnt -= 1
        if cnt == 0:
            return p[:i+1], p[i+1:]
def prof(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == "(":
            cnt += 1
        elif u[i] == ")":
            cnt -= 1
        # 균형잡힌 문자열
        if cnt < 0:
            return False
    # 올바른 문자열
    return True

def solution(p):
    if p == "":
        return ""
    u, v = divide(p)

    if prof(u):

        return u + solution(v)
    else:
        tmp = "(" + solution(v) + ")"
        reverse = ""
        for i in u[1:-1]:
            if i == "(":
                reverse += ")"
            else:
                reverse += "("
        tmp += reverse

        return tmp

    return
def sol(p):
    print(solution(p))
sol(p)