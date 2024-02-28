order = [4, 3, 1, 2, 5]


def solution(order):
    answer = 0
    stack = list()
    box = [i for i in range(1, len(order) + 1)]
    box = box[::-1]
    order = order[::-1]
    while True:
        box_check = False
        if box:
            # 박스 순서에 맞을때
            if order[-1] == box[-1]:
                box.pop()
                order.pop()
                answer += 1
                box_check = True
        stack_check = False
        if stack:
            # stack 순서에 맞을때
            if order[-1] == stack[-1]:
                stack.pop()
                order.pop()
                answer += 1
                stack_check = True
        if box_check is False and stack_check is False:
            if box:
                stack.append(box[-1])
                box.pop()
            else:
                break

    return answer
solution(order)